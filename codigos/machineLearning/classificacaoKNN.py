import math
import numpy as np
import matplotlib.pyplot as plt

amostras = []

with open('dataset1.data', 'r') as f :
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras.append(list(map(int, atrib)))



def info_dataset(amostras):
    rotulo1, rotulo2 = 0,0
    for amostra in amostras:
        if (amostra[-1] == 1):
            rotulo1 += 1
        else:
            rotulo2 += 1
   
    return [len(amostras), rotulo1, rotulo2]



# p = parametro de porcentagem de grupo de treinamento
for p in np.arange(0.1,0.9,0.1):
    _,rotulo1, rotulo2 = info_dataset(amostras)


    treinamento, teste = [],[]
    max_rot1, max_rot2 = int(p * rotulo1), int(p * rotulo2)
    tot_rot1, tot_rot2 =0,0  #treinamento

    for amostra in amostras:
        if(tot_rot1 +tot_rot2) < ( max_rot1 + max_rot2):
            treinamento.append(amostra)
            if(amostra[-1] ==1 and tot_rot1 < max_rot1):
                tot_rot1 += 1
            else:
                tot_rot2 += 1
        else:
            teste.append(amostra)


    #print (info_dataset(teste))
    #print (info_dataset(treinamento))


    def dist_eucl(v1,v2):
        v1, v2 = np.array(v1), np.array(v2)
        diff = v1 - v2
        quad_dist = np.dot(diff, diff)
        return math.sqrt(quad_dist)


    def knn(treinamento, nova_amostra, K):
        dists, tam_treino = {}, len(treinamento)
        for i in range(tam_treino):
            d = dist_eucl(treinamento[i], nova_amostra)
            dists[i] = d
            
        qt_rt1, qt_rt2 = 0,0
        for j in sorted(dists, key = dists.get)[:K] :
           if treinamento[j][-1] == 1:
               qt_rt1 += 1
           else:
               qt_rt2 += 1   
        
            
        if qt_rt1>qt_rt2:
            return 1
        else:
            return 2


    #print(teste[0][-1])
    #print(knn(treinamento, teste[0], 3))
    plotarray = []
    print('Resultado para p = '+ str(p))
    for k in range(3,30):
        
        result_certo = 0

        for t in teste:
            if knn(treinamento,t, k) == t[-1]:
                result_certo += 1
        plotarray.append(float((result_certo * 100) / (len(teste))))      
        print('Porcentagem K= '+str(k) + ' : ' + str((result_certo * 100) / (len(teste)))) 

    print (plotarray)
    plt.plot(plotarray, label = (str(p*100)+'% perc treinamento'))
    plt.legend(loc='lower right')

plt.show()

