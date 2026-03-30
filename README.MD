# 🧠 OSRS Intelligent Multi-Agent System

## 📌 Visão Geral

Este projeto implementa um sistema multi-agente utilizando **LangGraph + LangChain**, capaz de:

* Consultar dados reais de jogadores via API (TempleOSRS)
* Responder perguntas baseadas em conhecimento (RAG)
* Executar ferramentas específicas (tools)
* Realizar fallback para LLM quando necessário

O sistema é projetado com foco em **separação de responsabilidades**, **controle de fluxo explícito** e **extensibilidade**.

---

## 🎯 Objetivo

Construir um agente inteligente que:

> Recebe uma pergunta do usuário → decide a melhor estratégia → executa → responde de forma confiável

---

## 🧱 Arquitetura Geral

```text
User Input
   ↓
Router Node
   ├── Tool Agent (API TempleOSRS)
   ├── RAG Agent (Base de conhecimento de quests)
   └── Chat Agent (LLM fallback)
            ↓
        Resposta final
```

---

## ⚙️ Componentes do Sistema

### 🧭 1. Router Agent

Responsável por classificar a intenção da pergunta do usuário.

#### Tipos de rota:

* `tool` → quando envolve dados de jogador
* `rag` → quando envolve conhecimento de quests
* `chat` → fallback geral

#### Estratégia:

* Abordagem híbrida:

  * Regras simples (keywords)
  * LLM para classificação ambígua

---

### 🛠️ 2. Tool Agent (TempleOSRS API)

Executa chamadas reais para API externa.

#### 🔹 Tool 1 — Player Stats

Consulta estatísticas do jogador.

* Endpoint:
  https://templeosrs.com/api/player_stats.php

* Input:

  * username

* Output:

  * níveis de skills
  * total level
  * dados do jogador

---

#### 🔹 Tool 2 — Pet Count

Consulta número de pets do jogador.

* Endpoint:
  https://templeosrs.com/api/pets/pet_count.php

* Input:

  * username

* Output:

  * quantidade de pets

---

### 📚 3. RAG Agent (Quests)

Utiliza base de conhecimento local construída previamente.

#### Responsável por:

* responder perguntas sobre quests
* fornecer instruções
* evitar alucinação

#### Fonte:

* arquivos `.txt` com conteúdo de quests

---

### 💬 4. Chat Agent (Fallback)

Utilizado quando:

* não há necessidade de tool
* não há contexto no RAG
* perguntas abertas

---

## 🔁 Fluxo de Execução

```text
1. Usuário envia pergunta
2. Router classifica intenção
3. Sistema direciona:
   - Tool → executa API
   - RAG → busca contexto + LLM
   - Chat → LLM direto
4. Retorna resposta final
```

---

## 🧠 Estratégia de Decisão (Routing)

### Regras iniciais

| Tipo | Exemplos                                      |
| ---- | --------------------------------------------- |
| Tool | "stats do player Zeah", "quantos pets tenho?" |
| RAG  | "como fazer Dragon Slayer?", "quest guide"    |
| Chat | "melhor skill?", "dicas gerais"               |

---

## 📦 Funcionalidades

### ✔️ Tool Calling

* Integração com API externa
* Execução controlada via node
* Tratamento de erros

---

### ✔️ RAG (Retrieval-Augmented Generation)

* Busca semântica com FAISS
* Contexto estruturado
* Respostas grounded

---

### ✔️ Multi-Agent Routing

* Separação clara de responsabilidades
* Fluxo explícito com LangGraph

---

### ✔️ Fallback Inteligente

* Quando RAG não encontra resposta
* Quando pergunta é genérica

---

## ⚠️ Tratamento de Erros

### Tool Agent

* usuário inválido
* API indisponível
* resposta vazia

### RAG

* contexto irrelevante
* nenhum documento encontrado

---

## 🧠 Decisões de Design

### ✔️ LangGraph como orquestrador

* controle explícito do fluxo
* previsibilidade

### ✔️ Nodes como funções puras

* fácil teste
* baixo acoplamento

### ✔️ Separação de pipelines

* ingestão (offline)
* inferência (online)

---

## 🚀 Evoluções Futuras

* Persistência de sessões (memória real)
* Re-ranking de documentos (RAG)
* Cache de respostas
* Mais tools (XP calculator, GP/hour)
* Interface web (Streamlit / FastAPI)

---

## 📌 Requisitos Técnicos

* Python 3.11+
* LangChain
* LangGraph
* FAISS
* Gemini API

---

## 🧠 Insight Central

> Este projeto demonstra como transformar um LLM em um sistema inteligente através de:
>
> * controle de fluxo
> * integração com dados externos
> * separação de responsabilidades

---

## 🏁 Status

🚧 Em desenvolvimento — foco em arquitetura e aprendizado avançado de agentes.
