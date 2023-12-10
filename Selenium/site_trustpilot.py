#pip install selenium
#pip install webdriver-manager

def mesParaNumero(mes:str):
    return {
            'janeiro': 1,
            'fevereiro': 2,
            'março': 3,
            'abril': 4,
            'maio': 5,
            'junho': 6,
            'julho': 7,
            'agosto': 8,
            'setembro': 9, 
            'outubro': 10,
            'novembro': 11,
            'dezembro': 12
    }[mes.lower()]

def tratarData(conteudo:str):
    from datetime import datetime
    
    conteudo = conteudo.replace("Data da experiência: ","")
    conteudo = conteudo.replace(" de ","/")
    posicao=conteudo.find('/')
    dia = str(conteudo[0:posicao])
    mes = str(mesParaNumero(conteudo[posicao+1:-5]))
    ano = str(conteudo[-4:])
    
    data = dia+'/'+mes+'/'+ano

    return datetime.strptime(data, '%d/%m/%Y').date()

def tratarNota(nota):
    posicao = nota.find('Classificada ')

    if posicao > -1:
        posicao += 13
        return nota[posicao:1]
    else:
        return 0

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #método para localizar elementos

servico = Service(ChromeDriverManager().install()) #Identifica qual a versão do Chrome utilizada e instala ChromeDriverManager correspondente.

navegador = webdriver.Chrome(service=servico) #Define o browser a ser utilizado

#Site a navegar
navegador.get("https://pt.trustpilot.com/review/empresa.pt")

try:
    #Botão cookies - clica no botão quando aparecer da primeira vez
    navegador.find_element('xpath','//*[@id="onetrust-accept-btn-handler"]').click()
except:
    print("")

try:
    paginar = True

    lista =[]

    while paginar:
        for i in range(4,25):
            if i != 14:
                avaliador = navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/aside/div/a/span').text                
                
                notaObj = navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/section/div[1]/div[1]/img')
                nota = (tratarNota(notaObj.get_attribute('outerHTML')))
                
                avaliacao = navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/section/div[2]/p[1]').text
                avaliacao = avaliacao.replace('\n',' ') #Remove quebra de linha
                
                dataAvaliacao= tratarData(navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/section/div[2]/p[2]').text)
                
                lista.append([dataAvaliacao,nota,avaliador,avaliacao])
        
        if i == 24:
            #Botão Próximo
            navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div[26]/nav/a[4]').click()
        else:
            paginar = False

except:
     print("Deu except")

for item in lista :
    print(item)

