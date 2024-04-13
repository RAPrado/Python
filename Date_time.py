#Reference : https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
from datetime import date

data_atual = date.today()
print(data_atual) #2024-03-28

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)
print(data_em_texto) #28/3/2024

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto) #28/03/2024

#------------------------------------------------------------------------------------
#Working with date time
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
print(data_e_hora_em_texto) #28/03/2024

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto) #28/03/2024 10:35

data_e_hora_em_texto1 = '01/03/2024 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto1, '%d/%m/%Y %H:%M')
print(data_e_hora) #2024-03-01 12:30:00
