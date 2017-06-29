class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def toString(self):
        print (str(self.nome) + " ; " + str(self.idade))

    def semParam():
        print(self.nome)

pess = Pessoa('maria', 15)


print(pess.nome)
print(pess.idade)
pess.toString()


class Estudante(Pessoa):  #herança de classes , estudante herda de Pessoa
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome,idade)    #reutiliza definicoes da superclasse
        self.matricula = matricula


    def getMatricula(self):
        print(self.matricula)



estu=Estudante('Marcelo',21, 1222121)

estu.getMatricula()


class Robo:
    def __init__(self, x, y):
        self.x = x
        self.y=y


class Robo3d(Robo):
    def __init__(self, x,y,z):
        super(Robo3d, self).__init__(x,y)
        self.z =z


roboz = Robo3d(2,3,4)

print(roboz.x , roboz.y, roboz.z)
