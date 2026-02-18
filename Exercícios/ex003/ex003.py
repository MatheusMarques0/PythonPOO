class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo # linha 20 -> saldo de 3000 para c1
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo\n"


    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito autorizado de R${valor:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} autorizado na conta {self.id}")


c1 = ContaBancaria(112, "Gustavo", 3000)
print(c1)
c1.depositar(600)
print(c1)
c1.sacar(9000)
print(c1)

