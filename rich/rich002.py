from rich import print
from rich.panel import Panel

caixa = Panel(input(str("Digite algo: ")), title="Resposta", style="blue", width=35)
print(caixa)