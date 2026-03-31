# OSRS Multi Agent - Project Notes

Este documento serve como um guia "step by step" de como este projeto foi concebido e implementado, além de descrever o propósito e a importância de cada parte da sua arquitetura.

## Histórico de Implementação (Últimos Commits)
A evolução do projeto ocorreu em fases principais:
- **Estruturação Inicial**: Criação da estrutura base de diretórios e definição das dependências do projeto (`requirements.txt`), além de configurações do `git` (`.gitignore`).
- **Core Configuration**: Implementação do sistema de configurações usando `pydantic_settings` e carregamento de variáveis do `.env` aplicando boas práticas de desenvolvimento (substituindo chamadas diretas de `os.getenv`).
- **Modelos (LLM & Embeddings)**: Integração com o Google Generative AI (Gemini), com funções centralizadas de setup em `llm.py` e configuração do modelo de embedding em `embeddings.py`.
- **Ferramentas (Tools)**: Criação de clientes de API e serviços (ex: `TempleOsrsClient`, `TempleOsrsService`) para buscar informações e estatísticas de jogadores de Old School RuneScape a partir do portal TempleOSRS.
- **Agentes (Agents)**: 
  - `ChatAgent`: Implementação inicial de um agente conversacional ("chat") focado no domínio OSRS e com prompts pré-definidos.
  - `ToolAgent`: Agente especializado em executar roteamentos e gerenciar a execução correta das ferramentas de API a partir de inputs estruturados.
- **Testes e Entrada**: O arquivo `main.py` foi configurado para executar testes iniciais simulando requisições ao `ToolAgent`.

---

## Passo a Passo para Implementar e Rodar esse Projeto

### Passo 1: Preparar o Ambiente
1. Clone este repositório.
2. Crie um ambiente virtual para isolar as dependências e ative-o:
   - `python -m venv venv`
   - Linux/Mac: `source venv/bin/activate` | Windows: `venv\Scripts\activate`
3. Instale as dependências listadas:
   `pip install -r requirements.txt`

### Passo 2: Configurar as Variáveis de Ambiente
1. Crie um arquivo `.env` na raiz do projeto.
2. Preencha as configurações essenciais (estas refletem as exigências no arquivo `settings.py`):
   ```env
   PROVIDER=string
   GOOGLE_API_KEY=sua_chave_do_google_ai_studio
   MODEL=gemini-1.5-flash # ou outro modelo desejado
   EMBEDDING_MODEL=models/embedding-001
   TAVILY_API_KEY=sua_chave_ou_vazio
   ```

### Passo 3: Executando Aplicação
1. Se desejar, atualize o arquivo `app/main.py` para testar diferentes entradas, como alterar o nome do usuário (`username="Seu Nome no Jogo"`).
2. Execute diretamente o ponto de entrada usando:
   `python -m app.main`

---

## Arquitetura e Importância de Cada Arquivo

O projeto adota uma arquitetura modular que separa responsabilidades ("Clean Architecture" simplificada). Abaixo, a explicação de cada parte e a importância técnica dos arquivos:

### 1. `app/core/`
Esta camada contém as bases técnicas globais de configuração e a inicialização de instâncias críticas.
- **`config/settings.py`**: Utiliza o `BaseSettings` do Pydantic para carregar, converter e validar as variáveis do arquivo `.env`. 
  - **Importância:** Centraliza as chaves de API, garante type-safety e valida se as chaves existem antes que a aplicação suba propriamente, sendo um princípio de segurança e boas práticas.
- **`models/llm.py`**: Contém a configuração de inicialização do LLM (ex: `GoogleGenerativeAI`). 
  - **Importância:** Mantém a parametrização do modelo restrita a um único local, permitindo instanciar o modelo facilmente nos Agentes em vez de ficar repetindo chaves ou temperaturas de geração de texto no código.
- **`models/embeddings.py`**: Retorna instâncias responsáveis pela conversão de texto em embeddings vetoriais. 
  - **Importância:** Esta conversão de texto será altamente necessária em recursos de RAG (Busca e Geração aumentadas), preparando os recursos cognitivos do agente.

### 2. `app/tools/`
Aqui ficam as integrações externas e as "habilidades" que nossos agentes usarão.
- **`templeosrs/client.py`**: Faz chamadas limpas e diretas (usando `requests`) para a API de estatísticas externas `templeosrs.com`. 
  - **Importância:** Cumpre apenas a função de "HTTP request", não sabendo lidar com exceções de negócio da aplicação (separação de papéis).
- **`templeosrs/service.py`**: Envolve as chamadas do `client.py` nas regras da nossa aplicação e blinda erros usando blocos `try/except`. 
  - **Importância:** Os agentes *precisam* de previsibilidade. O serviço mastiga e formata os retornos no padrão comum `ToolResult` a fim de garantir que um erro de rede não quebre todo o pipeline sem controle.
- **`templeosrs/schemas.py`**: Especifica os contratos de dados usando Pydantic/Dataclasses. (Ex: classe estruturada de Output para erros ou sucesso).

### 3. `app/agents/`
Lógica que guia o comportamento inteligente. São fragmentados pela responsabilidade.
- **`chat_agent/`**: 
  - `agent.py`: Wrapper principal do agente conversacional, constrói as mensagens a partir do histórico humano e as envia pro LLM do `get_llm()`.
  - `prompt.py`: Armazena rigidamente o comportamento core (`SystemMessage`), e restrições semânticas que o modelo de LLM precisa assumir ao responder.
  - `schema.py`: Os contratos de input (ex `ChatInput`).
- **`tool_agent/`**: 
  - `agent.py`: Atualmente simula um coordenador ou roteador (um router agent). Determina *qual* ferramenta da OSRS vai rodar, mediante o parâmetro injetado, e lida com o repasse pra camada de serviço (Service).
  - `schema.py`: Estrutura de dados `ToolAgentInput` ditando como pedir o uso de alguma ferramenta explicitamente.

### 4. `app/main.py`
Seu principal ponto de partida ou arquivo de *Sandbox*. 
- **Importância:** Une a lógica solta, instanciando os Agentes isolados e passando dados concretos à eles para validar a execução (fluxo de testes funcional).
