#Referência : https://youtu.be/ZwfZlqTzsuA
#             https://github.com/Renatoelho/analise-sentimento-python-chatgpt

from api_key import API_KEY

import requests
import json

def avaliar_opiniao(texto: str) -> str:
    try:
        headers = {"Authorization":f"Bearer {API_KEY}", "Content-Type": "application/json"}

        #Visualizar os modelos do Chat Gpt
        #link = "https://api.openai.com/v1/models"
        #requisicao = requests.get(link, headers=headers)
        #print(requisicao)
        #print(requisicao.text)
        
        link = "https://api.openai.com/v1/chat/completions"
        id_modelo = "gpt-3.5-turbo"
        
        body_mensagem = {
            "model": id_modelo,
        
            #Exemplo 1 - Descomentar a linha abaixo se for usar.
            #"messages":[{"role": "user","content": "Escreva uma análise sobre o"
            #             f"texto: '{texto}'"}]
        
            #Exemplo 2 - Descomentar a linha abaixo se for usar.
            "messages":[{"role": "user","content": "Responda em uma única palavra, sendo positivo, negativo ou neutro o sentimento contido no seguinte "
                         f"texto: '{texto}'"}]
         }
        
        body_mensagem = json.dumps(body_mensagem)
        
        requisicao = requests.post(link, headers=headers, data=body_mensagem)
        
        if requisicao.status_code == 200:
            return requisicao.json()["choices"][0]["message"]["content"]
        else:
            print("Retorno com erro : " + str(requisicao.status_code))

    except Exception as _:
        return "Erro na execução da API"


from avaliacoes import avaliacoes_clientes

for texto in avaliacoes_clientes:
    avaliacao = avaliar_opiniao(texto)
   
    print(f"'{texto}' é um sentimento: {avaliacao}")
