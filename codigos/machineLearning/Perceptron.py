import random
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas = 1000, limiar = -1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = []
        self.n_epocas = 0

    def degrau(self,x):
        if x>=0:
            return 1
        return 0
    
    def treinar(self):
        for amostra in self.amostras:
            amostra.insert(0, -1)
    
        for i in range(self.n_atributos):
            self.pesos.append(random.random()) #para cada atributo adiciona um peso inicial aleatorio 
    
        self.pesos.insert(0, self.limiar) # esse é o valor de teta

        n_epocas = 0
        
        while True:
            erro = False #erro inicialmente nao existe
            for j in range(self.n_amostras):
                u = 0
                for k in range(self.n_atributos + 1):
                    u += self.pesos[k]*self.amostras[j][k]
                y = self.degrau(u)
                if y != self.saidas[j]:
                   for k in range(self.n_atributos + 1):
                       self.pesos[k] = self.pesos[k] + self.taxa_aprendizado * (self.saidas[j]-y) * self.amostras[j][k]
                   erro = True
            n_epocas += 1
            if not erro or n_epocas > self.epocas:
                break

        self.n_epocas = n_epocas
        
        
#OR

entradas = [[0,0],[0,1],[1,0],[1,1]]
saidas = [0,1,1,1]
        
        
rede = Perceptron(entradas, saidas)
rede.treinar()
vetx = []
vety = []
for i in np.arange(0.01,0.8, 0.01):
    rede = Perceptron(entradas, saidas,taxa_aprendizado=i, epocas = 1000, limiar = -1)   
    rede.treinar()
    a = rede.n_epocas
    vetx.append(a)
    vety.append(i)

plt.plot(vety,vetx, label = 'taxa de aprend= '+(str(i)))
plt.show()
