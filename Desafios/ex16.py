from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return print(f"Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo")

c1 = Funcionario("Maria", "Administração", "Diretora")
c1.apresentar()

c2 = Funcionario("Pedro", "TI", "Programador")
c2.apresentar()

#Versão Curso em Vídeo

class func:
    empresa = "Curso em Vídeo"

    def __init__(self, no, se, ca):
        self.no = no
        self.ca = ca
        self.se = se

    def apresen(self) -> str:
        return f":handshake: Olá. sou [blue]{self.no}[/] e sou {self.ca} do setor de {self.se} da empresa {func.empresa}"

c3 = func("Maria", "Administração", "Diretora")
print(c3.apresen())