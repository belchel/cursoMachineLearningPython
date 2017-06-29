import numpy as np

a = np.array([10, 20, 30, 40])

print(a)


matriz= np.array([[1,2],[3,4]])

print(matriz)

print(matriz[1][1])

print(matriz[1,:]) #2ª linha

print(matriz[:,0]) #1ª coluna


print(matriz.transpose())


print(matriz.sum())

print(matriz.argmax())

print(matriz.argmin())

print(matriz.mean())

print(matriz.diagonal())


print(matriz.ndim)



print(np.arange(1,1000001).sum())



mydata = np.arange(0,20)
print(mydata)

mat2=np.reshape(mydata,(5,4))

print(mat2)


print(mat2.item(5))


a = np.array([[1,2],[3,4]])

a = np.append(a,[[5,6]], axis=0) # axis corresposte ao eixo, ou a dimensao
print(a)


a= np.delete(a,1, 0) # delete(matriz,posicao, eixo)

print(a)


a = np.append(a,[[7,8]], axis=0) # axis corresposte ao eixo, ou a dimensao
print(a)


a= np.delete(a,1, 1) # delete(matriz,posicao, eixo) - eixo é opcional

print(a)


a= np.tile([1,2,3],3)

print(a)

a = np.array([[1,2],[3,4]])
a=np.tile(a,2)

print(a)

a = np.ones((4,3))

print(a)

a = np.zeros((2,1))

print(a)

a = np.eye(6) # cria matriz identidade de ordem 6

print(a)


a = np.array([[1,2],[3,4],[5,6]])

print (a[a>3])  # retorna todos os elementos maiores q 3

idx = (a>2)

print(idx)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6]])
print(B)

C = np.concatenate((A,B.T),axis=1)

print(C)
