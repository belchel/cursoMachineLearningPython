import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train= pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
cols = ['shoe size','height']
cols2 = ['class']

x_train = train.as_matrix(cols)
y_train = train.as_matrix(cols2)
x_test = test.as_matrix(cols)
y_test = test.as_matrix(cols2)


knn = KNeighborsClassifier(n_neighbors=3, weights='distance') # vizinhos mais próximos terão um peso maior no calculo


knn.fit(x_train,y_train.ravel())

output = knn.predict(x_test)

perc_acertos = knn.score(x_test, y_test)

print(perc_acertos)


