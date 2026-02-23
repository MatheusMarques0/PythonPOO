#from rich.panel import Panel
#from rich import print #Precisa dele para Rodar o Panel
#
#class Produto:
#
#    def __init__(self, nome = "Sem Registros", preco = 0.0):
#        self.nome = nome
#        self.preco = preco
#
#    def etiqueta(self):
#        return Panel(f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}", title="Produto", width=35)
#
#p1 = Produto("iPhone 17 Pro Max", 25000.85)
#p2 = Produto("Notebook Gmaer", 8_000)
#
##rint(p1.etiqueta())

# Versão Curso Em Vídeo
from rich.panel import Panel
from rich import print #Precisa dele para Rodar o Panel

class Produto:

    def __init__(self, nome = "Sem Registros", preco = 0.0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, " ")}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:.2f}"
        conteudo += f"{precof.center(30, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)

p1 = Produto("iPhone 17 Pro Max", 25000.85)
p2 = Produto("Notebook Gmaer", 8_000)

print(p1.etiqueta())
