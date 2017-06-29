import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('iris.txt', delimiter=",", usecols=(0,1,2,3))


plt.plot(data[:50,0], c ='Red' , ls=':', marker='s' , ms=2, label = 'Comp. Sepala iris Setosa') # 1ª coluna dos 50 primeiros elementos 
plt.plot(data[50:100,0], c ='Blue' , ls='-', marker='s' , ms=2, label = 'Comp. Sepala iris Versicolor')
plt.plot(data[100:150,0], c ='Green' , ls=':', marker='s' , ms=2, label = 'Comp. Sepala iris Virginica')
plt.legend(loc='upper left')
plt.show()
