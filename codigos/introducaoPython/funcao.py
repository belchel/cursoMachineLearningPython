def soma(a, b):
    return a+b

print(soma(1,2))


def somaSemLimite(*args):
    return sum(args)

print(somaSemLimite(1,2,3,4))

print(somaSemLimite())


imprimir = print

imprimir('babababa')


def fat(n):
    if n == 0 or n == 1:
        return 1
    return n * fat (n-1)


print(fat(5))


def paramDefault(nome='desconhecido'):
    print(nome)


paramDefault()
paramDefault('ComParam')


def somarComFunc(x,y,z,g):
    return x+g(y,z)



def f(n1,n2):
    return n1*n2

def h(n1,n2):
    return n1/n2

print(somarComFunc(1,2,3,f))

print(somarComFunc(1,2,3,h))


lamb = lambda x:x*2
print(lamb(4))



def somaVariado(*args):
    print(args)  #tupla de valores

def somaVariado2(*args):
    print(*args)  #desempacota cada elemento

def soma3elems(a,b,c):
    print(a,b,c)

somaVariado(1,2,3)
somaVariado2(1,2,3)
soma3elems(*(1,2,3))
soma3elems(*[1,2,3])

