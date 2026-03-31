from datetime import datetime

def date_to_epoch() -> int:
    now = datetime.now().strftime("%d/%m/%Y")

    # Define o formato brasileiro: Dia/Mês/Ano
    date_format = "%d/%m/%Y"
    
    # Converte a string para um objeto datetime
    # Por padrão, se a hora não for informada, ele considera 00:00:00
    date_obj = datetime.strptime(now, date_format)
    
    # Converte o objeto para o Unix Timestamp (float) e transforma em inteiro
    epoch = int(date_obj.timestamp())
    
    return epoch