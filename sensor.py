import requests
import random
import time
from datetime import datetime

# Inicialize o ID
dado_id = 0  

# Loop gerar e enviar dados
while True:
    temperatura = random.uniform(0, 45)
    umidade = random.uniform(0, 100)
    luminosidade = random.uniform(0, 100)

    # Incremente o ID a cada envio de dados
    dado_id += 1

    # Obtenha a data e hora atual no formato "YYYY-MM-DD HH:MM:SS"
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # dicionário com os dados a serem enviados            chave/id
    dados = {
        'id': dado_id,
        'temperatura': temperatura,
        'umidade': umidade,
        'luminosidade': luminosidade,
        'horario': horario
    }

    # Envie os dados para o servidor local usando uma solicitação POST
    response = requests.post('http://localhost:5000/dados', json=dados)

    print(response.json())

    time.sleep(10)
