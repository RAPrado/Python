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

6. Execute o compando abaixo, no cmd, para saber a versão pip e com isso validar que a instalação deu certo:<p>
 **pip --version**

  Se deu certo, deverá aparecer a tela abaixo : <p>
  <img src="/image/image03.png">
    
  Do contrário, pode aparecer a mensagem abaixo : <p>
  
  C:\Users\XXX>pip --version<br>
  Traceback (most recent call last):<br>
  File "runpy.py", line 197, in _run_module_as_main<br>
  File "runpy.py", line 87, in _run_code<br>
  File "C:\Users\XXX\Documents\Programacao\Python\python-3.9.13-embed-amd64\Scripts\pip.exe\__main__.py", line 4, in <module><br>
  ModuleNotFoundError: No module named 'pip'<p>

  <img src="/image/image02.png">
  
  Se ocoorer esse erro, então vá na pasta de instalação do Python, abra o arquivo **pythonXX._pth**, onde XX é a versão do Python, e adicione a linha **Lib\site-packages**, conforme o print abaixo, salve e feche o arquivo. <p>
  <img src="/image/image04.png">
  
7. Se quiser listar as bibliotecas instaladas :<p>
  **pip list**
8. Para instalar uma biblioteca :<p>
  **pip install < nome da bliboteca >**  

Referências :<p>
https://stackoverflow.com/questions/32639074/why-am-i-getting-importerror-no-module-named-pip-right-after-installing-pip<br>
https://www.geeksforgeeks.org/download-and-install-pip-latest-version/#windows<br>
https://neps.academy/br/blog/como-instalar-pip:-o-gerenciador-de-pacotes-do-python-no-windows
  
# c) Mudar o path do Windows para contemplar o Python e o PIP
1. Verificar se nas variáves de sistemas do Windows aparece a chamada para o Python e o PIP. Digitar VAR no pesquisar do Windows e dar enter.
2. Acessar a aba **Advanced**, e clicar no botão **Environment Variables**.
3. Na lista que aparece em **User variables for xxxx**, clique duas vezes em **Path**.
4. Irá abrir uma janela **Edit environment variable**, com os caminhos contidos no path.
5. Para adicionar o caminho do Python, clique no botão **New** e preencha com o endereço onde está o arquivo do Python.exe.
6. Para adicionar o caminho do PIP, clique no botão **New** e preencha com o endereço onde está o arquivo do PIP.exe.
7. Para garantir que o Python seja executado ao chamá-lo, mova o item **%USERPROFILE%\AppData\Local\Microsoft\WindowsApps** para o fim da lista, pois do contrário o Windows vai abrir o site da loja do Windows, para baixar o Python.
  
  Referência :<p>
  https://www.youtube.com/watch?v=G-HJg9CiPLw
  
# d) Criar um ambiente virtual com o **virtualenv** no Python
1. Execute o compando abaixo no cmd, para instalar o vitualenv:<p>
**pip install virtualenv**
 <img src="/image/image06.png">
    
2. Execute o compando abaixo no cmd, para ver a versão do vitualenv e ter certeza que está funcionando:<p>
**virtualenv --version**

3. Agora, para criar um ambiente virtual, execute o compando abaixo no cmd. Será criado uma pasta com o nome escolhido, na raiz do diretório em que você se encontre:<p>
**virtualenv nome_pasta_virtual**
<img src="/image/image07.png">

Caso dê o erro abaixo :<p>
<img src="/image/image08.png">

Crie essa pasta **DLLs** dentro da pasta do Python<p>
<img src="/image/image09.png">

4. É necessário ativar o ambiente virtual criado, para isso, entre na pasta criada, e acesse a pasta **Scripts**, e execute o arquivo **activate**
    **C:\Users\xxx\ml_estudo\Scripts>activate**
   
    Conforme o print abaixo, será exibido uma nova linha no cmd, onde no começo estará escrito entre parenteses, o nome da pasta virtual criada:
    <img src="/image/image10.png">

    Enquanto estiver ativa essa pasta virtual, ela será incluída no Path do Windows. Se quiser verificar, basta executar o comando Path no cmd :<p>
    **C:\path**
    
5. Quando quiser desativar o ambiente virtual criado, execute o arquivo **deactivate**<p>
    **C:\Users\xxx\ml_estudo\Scripts>deactivate**    
    
  Referência :<p>  
  https://acervolima.com/criacao-de-ambiente-virtual-python-no-windows-e-linux/<br>
  https://stackoverflow.com/questions/63784090/virtualenv-the-system-cannot-find-the-path-specified-python3-6-dll
    
# e) Instalar o Jupyter Notebook

  
Referência :<p>
https://jupyter.org/install
