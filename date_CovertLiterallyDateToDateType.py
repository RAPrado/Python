#Receives a date (Data da experiência: 10 de dezembro de 2023) written literally and converts it to a date
def tratarData(conteudo:str)-> date:
    from datetime import datetime
    
    conteudo = conteudo.replace("Data da experiência: ","")
    conteudo = conteudo.replace(" de ","/")
    posicao=conteudo.find('/')
    dia = str(conteudo[0:posicao])
    mes = str(mesParaNumero(conteudo[posicao+1:-5]))
    ano = str(conteudo[-4:])
    
    data = dia+'/'+mes+'/'+ano

    return datetime.strptime(data, '%d/%m/%Y').date()
