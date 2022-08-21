import os

Caminho = os.path.join("Pasta","SubPasta")    #Define as pastas a serem criadas
os.makedirs(Caminho, exist_ok=True)           #Cria as pastas, se existir sobrescreve
