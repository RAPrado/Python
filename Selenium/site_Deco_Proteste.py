#pip install selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #método para localizar elementos

navegador = webdriver.Chrome() #Define o browser a ser utilizado

#Site a navegar
navegador.get("https://www.deco.proteste.pt/reclamar/todas-as-reclamacoes?company=codigo da empresa")

try:
    #Botão cookies - clica no botão quando aparecer da primeira vez
    navegador.find_element('xpath','//*[@id="onetrust-accept-btn-handler"]').click()
except:
    print("")

try:
    import time
    from datetime import datetime
    origem = 'Deco_Proteste'
    paginar = True
    num_pagina =30

    #Cria o txt para gravar as avaliações
    f = open ('avaliacoes_' + origem + '.csv','w',encoding='utf-8')
    f.write('Origem|Data_Avaliacao|Nota|Avaliador|Data_Experiencia|Avaliacao|Titulo|Id_Reclamacao|Situacao|Qtd_Visualizacoes|Qtd_Comentarios|Data_Resposta|Resposta|Voltaria_Fazer_Negocio|Data_Captura\n')

    while paginar:
        for i in range(9,11):
            print('Entrou ',i)            

            #Inicia variáveis
            dataAvaliacao = ''
            nota = ''
            avaliador = ''
            dataExperiencia = ''
            avaliacao = ''
            titulo = ''
            id_reclamacao = ''
            situacao = ''
            qtd_visualizacoes = ''
            qtd_comentarios = ''
            data_resposta = ''
            resposta = ''
            voltaria = ''

            #Entra na reclamação
            navegador.find_element('xpath','//*[@id="publicComplaintsList"]/li['+str(i)+']/div/div/div/div[2]/h3/a').click()

            titulo = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[1]/div[1]/div[1]/div/h1').text
            titulo = titulo.replace('|',' ')  #Remove pipe
            titulo = titulo.replace('\n',' ') #Remove quebra de linha
            
            avaliador = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[2]/div[2]/div[2]/div/div[1]/p[1]').text
            
            dataAvaliacao = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[2]/div[2]/div[2]/div/div[2]/span').text
            dataAvaliacao = datetime.strptime(dataAvaliacao, '%d/%m/%Y').date()
            
            avaliacao = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[2]/div[2]/div[3]/div/div[1]/p').text
            avaliacao +=' Solução prentedida: ' + navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[2]/div[2]/div[3]/div/div[1]/div/ul/li').text
            avaliacao = avaliacao.replace('|',' ')  #Remove pipe
            avaliacao = avaliacao.replace('\n',' ') #Remove quebra de linha
            
            try:
                situacao = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[1]/div[2]/div[1]/div[2]/span[2]').text
            except:
                situacao =''

            try:
                data_resposta = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[4]/div/div[2]/div/div[2]/span').text
                data_resposta = datetime.strptime(data_resposta, '%d/%m/%Y').date()

                resposta = navegador.find_element('xpath','//*[@id="EscPublicThreadWrapper"]/div/div[4]/div/div[3]/div/div[1]/p').text
                resposta = resposta.replace('|',' ')  #Remove pipe
                resposta = resposta.replace('\n',' ') #Remove quebra de linha
            except:
                data_resposta =''
            
            #Grava no ficheiro
            f.write(origem + '|' + str(dataAvaliacao) + '|' + str(nota)  + '|' +  avaliador + '|' + str(dataExperiencia) + '|' + avaliacao + '|' + titulo + '|' +  id_reclamacao + '|' + situacao + '|' + str(qtd_visualizacoes) + '|' + str(qtd_comentarios) + '|' + str(data_resposta) + '|' + resposta + '|' + voltaria + '|' + (datetime.now()).strftime('%d/%m/%Y %H:%M:%S') + '\n')

            #Botão voltar do Chrome
            navegador.back()

        print('i vale :',i)
        if i == 10:        
            print('Avançou para página :',num_pagina)
            #Avança próxima página
            navegador.get("https://www.deco.proteste.pt/reclamar/todas-as-reclamacoes?company=codigo da empresa&page="+str(num_pagina))
            num_pagina +=1
        else:
            print('Parou')
            paginar = False
            f.close()

except Exception as e:
    f.close()
    
    mensagem = str(e)

    #Sempre quando terminar o loop na página, vai gerar erro pois tenta aceder a um objeto que não existe. Se for um erro diferente disso, então imprime.
    if mensagem.find('Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="__next"]') == -1:
        print(mensagem)
