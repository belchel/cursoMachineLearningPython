import numpy as np

x,y,z = np.loadtxt('dados.txt', skiprows=1, unpack=True) # unpack serve para carregar cada coluna numa variavel


print(x,y,z)


array = np.genfromtxt('dados2.txt', skip_header=1, filling_values=-1) # preenche com -1 em caso de MISSING

print(array)


valores = np.genfromtxt('novo.csv', delimiter=";", skip_header=1)

print(valores)
