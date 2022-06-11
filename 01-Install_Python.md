# a) Baixando o Python versão embeddable package para Windows
1. Baixar a versão desejada em https://www.python.org/
2. Descompactar o arquivo em uma pasta.
3. Essa versão vem sem o PIP, será necessário instalar a parte.

# b) Baixando o PIP para Python
1. Baixar o arquivo do pip em https://bootstrap.pypa.io/get-pip.py
2. Salvar na mesma pasta do Python.
3. Entrar no cmd e accessar a pasta do Python.
4. Executar  o compando :<p>
 **python get-pip.py**  
5. Aguardar a execução, conforme print abaixo :
  <img src="/image/image01.png">

6. Se quiser listar as bibliotecas instaladas :<p>
  **pip freeze**
7. Para instalar uma biblioteca :<p>
  **pip install < nome da bliboteca >**  

Referência :<p>
https://www.geeksforgeeks.org/download-and-install-pip-latest-version/#windows<p>
https://neps.academy/br/blog/como-instalar-pip:-o-gerenciador-de-pacotes-do-python-no-windows
  
# c) Mudar o path do Windows para contemplar o Python e o PIP
1. Verificar se nas variáves de sistemas do Windows aparece a chamada para o Python e o PIP. Digitar VAR no pesquisar do Windows e dar enter.
2. Acessar a aba **Advanced**, e clicar no botão **Environment Variables**.
2. Caso contrário, criar uma chamada com o nome de JAVA_HOME, e definir um caminho, como por exemplo : C:\Program Files\Zulu\zulu-11
3. Em path, validar se há a chamada para a pasta onde o Java foi instaldo : C:\Program Files\Zulu\zulu-11\bin, e mover isso, para o topo da lista.
  
  Referência :<p>
  https://www.youtube.com/watch?v=G-HJg9CiPLw
  
# d) Criar ambiente virtual para o Python


  
Referência :<p>
https://www.geeksforgeeks.org/download-and-install-pip-latest-version/#windows<p>
https://neps.academy/br/blog/como-instalar-pip:-o-gerenciador-de-pacotes-do-python-no-windows
