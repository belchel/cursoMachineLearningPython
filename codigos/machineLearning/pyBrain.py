import scipy
import numpy as np
import matplotlib.pyplot as plt
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

#passa as dimensoes dos vetores de entrada e da resposta
dataset = SupervisedDataSet(2,1)

dataset.addSample([1,1],[0])
dataset.addSample([1,0],[1])
dataset.addSample([0,1],[1])
dataset.addSample([0,0],[0])

network = buildNetwork(dataset.indim, 4 , dataset.outdim, bias = True)

trainer = BackpropTrainer(network, dataset, learningrate = 0.01, momentum=0.99)


for epoca in range(300):
    trainer.train()
##trainer.trainUntilConvergence()



test_data = SupervisedDataSet(2 ,1)

test_data.addSample([1,1],[0])
test_data.addSample([1,0],[1])
test_data.addSample([0,1],[1])
test_data.addSample([0,0],[0])

trainer.testOnData(test_data, verbose= True)
print(trainer.totalepochs)
