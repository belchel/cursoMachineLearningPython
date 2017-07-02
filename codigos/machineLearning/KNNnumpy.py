import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def convStr(x):
    if 'L' in str(x):
        return 1
    elif 'B' in str(x):
        return 2
    else:
        return 3
    
    
x = np.genfromtxt('dataset2.data', delimiter=',', usecols=(1,2,3,4))
y = np.genfromtxt('dataset2.data', delimiter=',', usecols=(0), converters = {0: convStr})



for p in np.arange(0.1,0.9,0.1):
    x_treino, x_teste, y_treino,  y_teste = train_test_split(x,y, test_size=p, random_state=42)
    plotarray = []
    print('Resultado para p = '+ str(p))
    for k in range(3,30):
        knn = KNeighborsClassifier(n_neighbors=k, p=2)

        knn.fit(x_treino, y_treino)

        result = knn.predict(x_teste)


        #perc_acertos = (np.sum(result ==y_teste)*100)/len(y_teste)
        perc_acertos = knn.score(x_teste, y_teste)
        plotarray.append(perc_acertos)
        print('Porcentagem K= '+str(k) + ' : ' + str(perc_acertos)) 

    plt.plot(plotarray, label = (str(p*100)+'% perc treinamento'))
    plt.legend(loc='lower right')

plt.show()



