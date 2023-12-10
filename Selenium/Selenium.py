#Exemplo de nagevação usando o Selenium no Chrome

#pip install selenium
#pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #método para localizar elementos 

servico = Service(ChromeDriverManager().install()) #Identifica qual a versão do Chrome utilizada e instala ChromeDriverManager correspondente.

navegador = webdriver.Chrome(service=servico) #Define o browser a ser utilizado

#Site a navegar
navegador.get("https://url")

try:
    paginar = True

    while paginar:
        for i in range(4,25):
            campoA = navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/section/div[2]/p[1]').text
            campoB= navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div['+str(i)+']/article/div/section/div[2]/p[2]').text

        if i == 24:
            #Botão Próximo
            navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div[26]/nav/a[4]').click()
        else:
            paginar = False
except:
     print("erro")

#Fecha o browser
navegador.close()

#Pegar o XPATH
#Clicar em Inspecionar o site com o botao direito mouse, selecionar o cursor, e na pagina clicar no obejto desejado, então no codigo que será selecionado no inspecionar, pressionar botão direito mouse, copy, e escolher opção xpath

#Achar todos objetos pelo xpath inteiro ou parcial
#avaliacoes = navegador.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div/div[3]/section/div[25]/article/div/section/div[2]/p[1]')

#Achar objeto específico
#navegador.find_element('xpath','//*[@id="__next"]/div/div/main/div/div[3]/section/div[4]/article/div/section/div[2]/p[1]')

#Eventos
#.click()
#.send_keys()
#navegador.find_element(By.NAME, "q") #Achar pelo name.



