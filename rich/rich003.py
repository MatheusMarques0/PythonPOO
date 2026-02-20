from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços", style="red")

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("Teclado", "R$ 100,00")

print(tabela)