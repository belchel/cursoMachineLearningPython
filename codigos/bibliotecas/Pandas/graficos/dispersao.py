#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset as dset

iris = dset.data('iris')

plt.scatter(iris['Sepal.Length'], iris['Sepal.Width'], sizes = 20* iris['Petal.Length'])

plt.show()


def specie_color(x):
    if x =='setosa':
        return 0
    elif x =='versicolor':
        return 1
    return 2



iris['SpeciesNumber'] = iris['Species'].apply(specie_color) #somente aceita numerico


plt.scatter( iris['Sepal.Length'], iris['Sepal.Width'], sizes = 20* iris['Petal.Length'],
             c=iris['SpeciesNumber'], cmap='viridis', alpha=0.4) #c= color  ,  cmap  = mapa de cores.

plt.show()
