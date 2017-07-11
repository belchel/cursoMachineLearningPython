import numpy as np
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
import matplotlib.pyplot as plt

entradas = np.genfromtxt('iris.data', delimiter=',', usecols=(0,1,2,3))
saidas = np.genfromtxt('iris.data', delimiter=',', usecols=(4))


#105 pra treino , 35 de cada

in_treino = np.concatenate((entradas[:35], entradas[50:85],entradas[100:135]))
out_treino = np.concatenate((saidas[:35], saidas[50:85],saidas[100:135]))

                                 
in_teste = np.concatenate((entradas[35:50], entradas[85:100],entradas[135:]))
out_teste = np.concatenate((saidas[35:50], saidas[85:100],saidas[135:]))


treinamento = SupervisedDataSet(4, 1)

for i in range(len(in_treino)):
    treinamento.addSample(in_treino[i], out_treino[i])


network = buildNetwork(treinamento.indim, 4 , treinamento.outdim, bias = True)


learn = 0.01
momentum = 0.1
epocas = 500
erros = []
x=[]
for it in np.arange(0.01,0.09, 0.01):
    x.append(it)
    trainer = BackpropTrainer(network, treinamento, learningrate = it, momentum=0.3)
    for epoca in range(200):
        trainer.train()

    test_data = SupervisedDataSet(4 ,1)

    for i in range(len(in_teste)):
        test_data.addSample(in_teste[i], out_teste[i])

    erros.append(trainer.testOnData(test_data, verbose= False))
##print(x)
##print(erros)
plt.plot(x, erros, label = 'erros', color='red', linewidth=1.5)
plt.show()
