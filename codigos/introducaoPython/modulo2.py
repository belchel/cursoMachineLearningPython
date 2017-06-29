from modulo1 import area_quad
import subdir.modulo3 as modulo3
import modulo1
import math



print(area_quad(2))
print(modulo1.perim_quad(4))
print(modulo1.area_ret(2,4))
modulo3.print7vezes('Hi')

print(math.cos(0.5))
print(math.sqrt(9))

print(math.factorial(6))


def area_quad(f):
    print(math.pow(f,2))


area_quad(9)
