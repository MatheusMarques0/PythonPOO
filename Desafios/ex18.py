from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo = "nulo", qtd = 0):
        self.titulo = titulo
        self.qtd = qtd

#métodos
    def analisar(self):
        kg = 82.40
        kgPessoa = 0.4
        totalCarne = self.qtd * kgPessoa
        custoTotal = totalCarne * kg
        precoPessoa = custoTotal / self.qtd
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/]\n"
        conteudo += f"cada participante comerá {kgPessoa}Kg e cada Kg custa R${kg:.2f}\n"
        conteudo += f"Recomendo [blue]Comprar {totalCarne:.3f}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R${custoTotal:.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${precoPessoa}[/] para participar."

        caixa = Panel(conteudo, title=f"{self.titulo}", width=100)
        print(caixa)



c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

#CONSIDERE:
#Consumo padrão: 400g por pessoa
#Preço: R$82,40/Kg

#quanto de carne deve ser comprado
#o custo total do churrasco
#preço por pessoa