#Declaração de Classe
class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    #Métodos de Instânica
    def Aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 21
g1.Aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Paulo"
g2.idade = 30
g2.Aniversario()
print(g2.mensagem())