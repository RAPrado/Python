#Referências : https://www.youtube.com/watch?v=Z3Fg-QkG6lk

#Metódo 1
pip install pyinstaller

pyinstaller.exe --onefile --windowed --icon=icone.ico programa.py #Ira criar um executável do programa.
#onde :
#--onefile : irá criar um único arquivo com tudo embutido.
#--windowed : oculta janela.
#--icon : define um ícone para o programa.
#Ao final, irá criar duas pastas, a build que pode ser excluída, e a dist, que conterá o executável.


#Metódo 2
pip install cx_Freeze

cxfreeze programa.py --target-dir pasta_destino
#Ira criar uma pasta com o executável e todos os arquivos necessários para execução.
