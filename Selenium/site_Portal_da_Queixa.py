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

    conteudo = conteudo.lower()
    conteudo = conteudo.replace("data de ocorrência: ","")
    conteudo = conteudo.replace(" de ","/")
    posicao=conteudo.find('/')
    dia = str(conteudo[0:posicao])
    mes = str(mesParaNumero(conteudo[posicao+1:-5]))
    ano = str(conteudo[-4:])
    
    data = dia+'/'+mes+'/'+ano

    return datetime.strptime(data, '%d/%m/%Y').date()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By #método para localizar elementos
navegador = webdriver.Chrome() #Define o browser a ser utilizado
#Site a navegar
navegador.get("https://portaldaqueixa.com/brands/empresa/complaints")

try:
    #Botão cookies - clica no botão quando aparecer da primeira vez
    navegador.find_element('xpath','//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()
except:
    print("")
try:
    import time
    from datetime import datetime
    origem = 'Portal_da_Queixa'
    paginar = True
    num_pagina =41

    #Cria o txt para gravar as avaliações
    f = open ('avaliacoes_' + origem + '.csv','w',encoding='utf-8')
    f.write('Origem|Data_Avaliacao|Nota|Avaliador|Data_Experiencia|Avaliacao|Titulo|Id_Reclamacao|Situacao|Qtd_Visualizacoes|Qtd_Comentarios|Data_Resposta|Resposta|Voltaria_Fazer_Negocio\n')

    while paginar:
        for i in range(1,11):
            print('Entrou ',i)

            #Só captura reclamações não classificadas como Privada
            if navegador.find_element('xpath','//*[@id="brand"]/div[2]/div/div[2]/div[2]/a[' + str(i) + ']/div/div[2]').text != 'Empresa - Reclamação privada':            
                #Entra na reclamação
                navegador.find_element('xpath','//*[@id="brand"]/div[2]/div/div[2]/div[2]/a['+str(i)+']/div').click()
    
                #Copia as informações
                try:
                    titulo = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[1]/h1').text
                except:
                    titulo = navegador.find_element('xpath','//*[@id="complaint-detail"]/div/div/div[2]/div[1]/div[1]/div/div[1]/h1').text                                         
                    
                titulo = titulo.replace('|',' ')  #Remove pipe            
    
                try:
                    situacao = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[1]/div/div').text
                except:
                    situacao = navegador.find_element('xpath','//*[@id="complaint-detail"]/div/div/div[2]/div[1]/div[1]/div/div[2]/div').text
                
                situacao = situacao.replace('|',' ')  #Remove pipe
                
                #Avaliador - faz tratamento pois as vezes muda o campo
                try:
                    avaliador = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/div[1]/a').text
                except:
                    try:
                        avaliador = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/div[1]/span').text
                    except:
                        avaliador = "Erro"
    
                avaliador = avaliador.replace('|',' ')  #Remove pipe
                
                #Data Avaliação - faz tratamento pois as vezes aparece mensagem que a data foi editada
                try:
                    dataAvaliacao = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/div[2]').text
                    if dataAvaliacao.find('(EDITADA') >-1:
                        dataAvaliacao=dataAvaliacao[:dataAvaliacao.find('(EDITADA')-1]
                    dataAvaliacao = tratarData(dataAvaliacao)
                except:
                    dataAvaliacao = ''
    
                avaliacao = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]').text
                avaliacao = avaliacao.replace('\n',' ') #Remove quebra de linha
                avaliacao = avaliacao.replace('|',' ')  #Remove pipe
                    
                #Data da ocorrência - faz tratamento pois o campo pode mudar de objeto no ecrã
                dataExperiencia = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div').text
                if dataExperiencia.find('Data de ocorrência') > -1:
                    dataExperiencia = tratarData(dataExperiencia)
                else:
                    dataExperiencia =  tratarData(navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]').text)
    
                id_reclamacao = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]').text
                id_reclamacao = id_reclamacao.replace('Reclamação ','')
                
                qtd_visualizacoes = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]').text
                qtd_visualizacoes = qtd_visualizacoes.replace(' visualizações','')
                
                qtd_comentarios = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[3]').text
                qtd_comentarios = qtd_comentarios.replace(' comentários','')
    
                if situacao != 'Aguarda resposta':
                    #DAta resposta - faz tratamento pois o campo pode mudar de objeto no ecrã
                    try:
                        data_resposta = tratarData(navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]').text)
                    except:
                        try:
                            data_resposta = tratarData(navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]').text)
                        except:
                            data_resposta = 'Erro'                
    
                    try:
                        resposta = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[2]').text
                        resposta = resposta.replace('|',' ')  #Remove pipe
                        resposta = resposta.replace('\n',' ') #Remove quebra de linha
                    except:
                        resposta = ''
    
                    if situacao == 'Resolvida':
                        try:
                            nota = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[1]/div/span').text
                            nota = nota[:nota.find('/')]
                        except:                        
                            nota = 0
        
                        #Voltaria a fazer negócio - faz tratamento pois o campo pode mudar de objeto no ecrã
                        try:
                            voltaria = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[4]/div/div[2]/div/div[1]/span').text
                        except:
                            try:
                                voltaria = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/span').text                                                   
                            except:
                                try:
                                    voltaria = navegador.find_element('xpath','//*[@id="brand"]/section/div/div[2]/div[2]/div[1]/div[2]/div[8]/div/div[2]/div/div[1]/span').text                                                   
                                except:
                                    voltaria = "Erro"
                
                        voltaria = voltaria.replace('Voltaria a fazer negócio? ','')
                    else:
                        nota = ''
                        voltaria = ''
                else:
                    data_resposta=''
                    resposta=''
                    
    
                #Grava no ficheiro
                f.write(origem + '|' + str(dataAvaliacao) + '|' + str(nota)  + '|' +  avaliador + '|' + str(dataExperiencia) + '|' + avaliacao + '|' + titulo + '|' +  id_reclamacao + '|' + situacao + '|' + str(qtd_visualizacoes) + '|' + str(qtd_comentarios) + '|' + str(data_resposta) + '|' + resposta + '|' + voltaria + '\n')
    
                #Limpa variáveis
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
    
                #Botão voltar do Chrome
                navegador.back()
                
                time.sleep(1)

        print('i vale :',i)
        if i == 10:        
            print('Avançou para página :',num_pagina)
            #Avança próxima página
            navegador.get("https://portaldaqueixa.com/brands/empresa/complaints?p="+str(num_pagina))
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
