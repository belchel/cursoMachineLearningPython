import pandas as pd
import numpy as np


dados = {'nomes':['Joao','Maria',np.nan,np.nan],
         'sexo':['M','F',np.nan,np.nan],
         'idade':[14,15,np.nan,6],
         'nota':[9,6,np.nan,9]}

df = pd.DataFrame(dados)


df3= df.dropna(how='all') #deleta apenas se todas as colunas estiverem vazias

#print(df3)
df['serie'] = np.nan

df['serie'].fillna(9, inplace=True)  #preenche com 9 em caso de vazio

print(df)


