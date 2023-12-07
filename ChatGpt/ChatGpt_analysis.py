#Referência : https://youtu.be/ZwfZlqTzsuA
#             https://github.com/Renatoelho/analise-sentimento-python-chatgpt

from senha import API_KEY

import requests
import json

headers = {"Authorization":f"Bearer {API_KEY}", "Content-Type": "application/json"}

#link = "https://api.openai.com/v1/models"
#requisicao = requests.get(link, headers=headers)
#print(requisicao)
#print(requisicao.text)

link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,

    #Exemplo 1 - Descomentar a linha abaixo se for usar.
    #"messages":[{"role": "user","content": "Escreva uma análise sobre o aquecimento global"}]

    #Exemplo 2 - Descomentar a linha abaixo se for usar.
    #"messages":[{"role": "user","content": "Responda em uma única palavra, sendo positivo, negativo ou neutro o sentimento contido no seguinte texto: Gosto muito de dia ensolarado"}]
 }

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)

if requisicao.status_code == 200:
    print(requisicao.json()["choices"][0]["message"]["content"])
else:
    print("Retorno com erro : " + str(requisicao.status_code))
