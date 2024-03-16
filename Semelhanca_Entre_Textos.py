#Compare two list and tells the degree of similarity.

#Reference :https://raisler-voigt.medium.com/estimando-a-similaridade-entre-textos-de-um-jeito-simples-usando-python-6c84a819f1c0
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def semelhanca_entre_textos(texto1, texto2):
    #Faz tocknização usando  unigramas e bigramas
    #ex. unigrama : {‘Isso’, ‘um’, ‘teste’, ‘de’,...}
    #ex. bigrama : {‘Isso um’, ‘um teste’, ‘teste de’...}
    #ex. tokenizando com Unigrams e Bigrams : {‘Isso’, ‘um’, ‘teste’, ‘de’,‘Isso um’, ‘um teste’, ‘teste de’...}
    vetor = CountVectorizer(analyzer = 'word',ngram_range=(1,2))
    semelhanca=[]

    for avaliacao1 in texto1:
        for avaliacao2 in texto2:
            a1, a2 = vetor.fit_transform([avaliacao1, avaliacao2])
            t1, t2 = a1.toarray(), a2.toarray()

            menor =np.amin([t1,t2], axis = 0)
            soma = np.sum(menor)
            conta = np.sum([t1,t2][0])
            perc = soma/conta
            semelhanca.append(perc)
            
    return semelhanca

Texto1 = ["""Isso é um teste de comparação entre duas listas"""]

Texto2 = ["""Isso não é um teste de comparação entre duas listas""",
         """Para que comparar esse texto"""]

print("O percentual de semelhança é de :",semelhanca_entre_textos(Texto1,Texto2))
#O percentual de semelhança é de : [0.9333333333333333, 0.0]