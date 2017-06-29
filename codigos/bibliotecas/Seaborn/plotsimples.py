import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1,10,100)




sns.set_style('ticks')
sns.set_style('white')


plt.plot(x, np.sin(x), 'b--')
plt.plot(x, np.cos(x), 'r--')
plt.show()


