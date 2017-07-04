from sklearn.datasets import load_boston
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt


#506 itens
#14 atributos

boston = load_boston()

K = 9

knn = KNeighborsRegressor(n_neighbors=K)

knn.fit(boston.data, boston.target)

obtido = knn.predict(boston.data);

plt.plot(boston.target, label = 'esperado', color = 'green')

plt.plot(obtido, label = 'obtido', color = 'red')



plt.show()


