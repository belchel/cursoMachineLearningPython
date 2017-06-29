import numpy


a = numpy.array([20,30,40,50])

print(a)


b = a[:]  #copia por referencia


b[0]=100 #mudando em b vai alterar em a tambem

print(a)
print(b)

  

c = a.copy()  #para fazer uma copia por valor, usar o copy()

print(c)

c[0] = 900


print(c)

print(a)
print(b)
