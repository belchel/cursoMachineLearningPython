from sklearn.datasets import load_boston
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import math

#506 itens
#14 atributos

boston = load_boston()

for K in range(3,21):

    knn = KNeighborsRegressor(n_neighbors=K)

    knn.fit(boston.data, boston.target)

    obtido = knn.predict(boston.data);

    somaErrosQuadrados=0
    for i in  range(0,len(boston.target)):
        somaErrosQuadrados += math.pow(boston.target[i] - obtido[i],2)

    erroQuadraticoMedio= somaErrosQuadrados/len(boston.target)

    print(erroQuadraticoMedio)

    #Utilizando o sklearn.metrics
    plt.scatter(K, mean_squared_error(boston.target,obtido))
    plt.text(K, mean_squared_error(boston.target,obtido), str("%.2f" % erroQuadraticoMedio))

plt.xticks(range(3,21))   
plt.show()
    




