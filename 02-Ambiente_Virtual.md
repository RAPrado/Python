# Criar um ambiente virtual com o **virtualenv** no Python
1. Execute o comando abaixo no cmd, para instalar o vitualenv:<p>
**pip install virtualenv**
 <img src="/image/image06.png">
    
2. Execute o comando abaixo no cmd, para ver a versão do vitualenv e ter certeza que está funcionando:<p>
**virtualenv --version**

3. Agora, para criar um ambiente virtual, execute o comando abaixo no cmd. Será criado uma pasta com o nome escolhido, na raiz do diretório em que você se encontre:<p>
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

6-Tente instalar algum pacote no ambiente virtual para testar se está funcionando. Caso dê o erro:<br>
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding<br>
Python runtime state: core initialized<br>
    
<img src="/image/image11.png">
