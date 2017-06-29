import pandas as pd

df = pd.DataFrame([['dado1',1212],['dado2',4431],['dado3',5633]])

print(df)

print(df.shape) #retorna as dimensoes do dataframe

df = pd.DataFrame([['dado1',1212],['dado2',4431],['dado3',5633]], columns = ['repositorio','linhas'])
    #columns cria nomes para as colunas

print(df)


print(df['repositorio'])  #retorna os elementos da coluna de nome repositorio

print(df['linhas'].mean())

print(df.iloc[1]) #retorna os elementos da linha 1

print(df.iloc[1]['linhas']) #retorna o elemento linhas da linha correspondente

df.index = pd.Index([2,5,9]) #associa cada indice a uma linha

print(df)

print(df.iloc[1])

print(df.ix[5])

df.index = df['repositorio'] #transforma a coluna em indice

print(df.ix['dado1'])

print(df)

del df['repositorio']  #como ficou duplicado, pode deletar a coluna 

print(df)

print(df.ix['dado1'])
