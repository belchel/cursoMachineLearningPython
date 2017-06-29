import numpy as np
import matplotlib.pyplot as plt

sal1 = np.array([100,200,300,400,500,150])
sal2 = np.array([300,400,100,30,600,200])
sal3 = np.array([400,500,900,800,700,500])



plt.plot(sal1, c = 'Red', ls='--', marker='s', label = 'Sal1')
plt.plot(sal2, c = 'Green',  marker='d', label = 'Sal2')
plt.plot(sal3, c = 'Blue',  marker='o', label = 'Sal3')
plt.legend(loc='upper left')
plt.show()


