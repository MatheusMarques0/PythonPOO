#Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto com nome idade.
    para criar um novo gafanhoto, use:
    variavel = Gafanhoto(Nome, Idade)
    """
    def __init__(self, n = "vazio", i = 0): #Dois Parâmetros
        self.nome = n
        self.idade = i

    #Métodos de Instânica
    def Aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.Aniversario()
print(g1)

g2 = Gafanhoto()
print(g2)

print(g1.__doc__) #Dunder Attribute
print(g1.__dict__) #Attribute
print(g1.__getstate__()) # Method
print(g1.__class__) #Class