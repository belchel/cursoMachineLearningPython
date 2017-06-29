#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset as dset


titanic = dset.data('titanic') #dados categoricos

titanic['class'].value_counts().plot(kind='bar') #histograma

plt.show()


titanic.groupby('survived')['class'].value_counts().plot(kind='bar') #histograma


plt.show()


titanic.groupby('survived')['class'].value_counts().plot(kind='pie') #pizza


plt.show()


titanic.groupby('survived')['class'].value_counts().hist()


plt.show()


fig, ax = plt.subplots()

plt.hist(titanic.groupby('survived')['class'].value_counts(), orientation='horizontal')

ax.ticklabel_format(style='plain')

plt.show()


plt.pie(titanic.groupby('survived')['class'].value_counts(),   autopct='%0d')

plt.show()

