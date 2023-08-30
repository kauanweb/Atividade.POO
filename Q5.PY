class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            print("O valor do depósito deve ser maior que zero.")
            return False

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente para efetuar o saque.")
            return False

conta = ContaCorrente(numero_conta="12345", nome_correntista="João")
print(f"Saldo inicial: R${conta.saldo}")

conta.deposito(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.saque(500)
print(f"Saldo após saque: R${conta.saldo}")

conta.alterarNome("João Silva")
print(f"Novo nome do correntista: {conta.nome_correntista}")
