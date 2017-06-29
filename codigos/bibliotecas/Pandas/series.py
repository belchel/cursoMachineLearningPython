import pandas as pd
import numpy as np

s = pd.Series([1,4,6,5,7,10,6]) #Serie é de apenas 1 dimensal = lista

print(s)

print(s.describe()) #retorna algumas informaçoes estatisticas da serie

print(s.mean()) # média da serie

print(s.median())   #valor mediano = ordenar de forma crescente e se a
                    #quantidade for impar, pega o valor que está no meio, se for
                    #par pega os dois que estao no meio soma e divide por 2

print(s.duplicated()) #retorna uma serie de booleanos indicando a posicao que esta duplicado


s2 = pd.Series([3,5,7])

s3 = s.append(s2)

print(s3)
