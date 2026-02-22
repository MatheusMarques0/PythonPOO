from rich.panel import Panel
from rich import print #Precisa dele para Rodar o Panel

class Produto:

    def __init__(self, nome = "Sem Registros", preco = 0.0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}", title="Produto", width=35)

p1 = Produto("iPhone 17 Pro Max", 25000.85)
p2 = Produto("Notebook Gmaer", 8_000)

print(p1.etiqueta())

