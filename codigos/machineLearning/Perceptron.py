import random
import numpy as np
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas = 1000, limiar = -1, func = 0):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = []
        self.n_epocas = 0
        self.func = func

    def degrau(self,x):
        if x>=0:
            return 1
        return 0
    
    def sinal(self,x):
        if x>=0:
            return 1
        return -1
    
    def funcao(self,x):
        if self.func == 0 :
            return self.degrau(x)
        elif self.func == 1:  
            return self.sinal(x)
    
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
                y = self.funcao(u)
                if y != self.saidas[j]:
                   for k in range(self.n_atributos + 1):
                       self.pesos[k] = self.pesos[k] + self.taxa_aprendizado * (self.saidas[j]-y) * self.amostras[j][k]
                   erro = True
            n_epocas += 1
            if not erro or n_epocas > self.epocas:
                break

        self.n_epocas = n_epocas
        
    def operacional(self, classificar):
        classificar.insert(0, -1)
        u = 0
        for k in range(self.n_atributos + 1):
            u += self.pesos[k]*classificar[k]
        y = self.funcao(u)
        print('Classe %d' % y)
        return y

        

#OR
entradas = [[0,0],[1,0],[1,1]]
saidas = [0,1,1]
                
rede = Perceptron(entradas, saidas)
rede.treinar()
rede.operacional([0,1])
rede.operacional([0,0])


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


#outra usando a sinal

entradas = [[0.1,0.4,0.7],[0.3,0.7,0.2],[0.6,0.9,0.8],[0.5,0.7,0.1]]
saidas = [1,-1,-1,1]
                
rede = Perceptron(entradas, saidas, func = 1)
rede.treinar()
rede.operacional([0.1,0.4,0.7])
rede.operacional([0.5,0.7,0.1])
rede.operacional([0.6,0.9,0.8])

