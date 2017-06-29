dicionario = {'Maria':4 , 'Pedro':5, 'Felipe':9}
print(dicionario['Pedro'])
dicionario['Pedro'] = 12
print(dicionario)
dicionario['Jose'] = 52
print(dicionario)


for k in dicionario:
    print(dicionario[k], end=' ')

print(dicionario.items())

print(dicionario.keys())

print(dicionario.values())

print('Maria' in dicionario)

