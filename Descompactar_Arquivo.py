import tarfile

Caminho = os.path.join("Pasta","SubPasta")         #Endereço da pasta   
tgz_Caminho = os.path.join(Caminho,"Arquivo.tgz")  #Nome do arquivo

Arquivo_tgz = tarfile.open(tgz_Caminho)
Arquivo_tgz.extractall(path=Caminho)
Arquivo_tgz.close()
