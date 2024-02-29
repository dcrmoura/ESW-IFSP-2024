from conta import Conta

class ContaPoupanca(Conta):
    def detalhes_conta(self):
        return f"\nConta Poupança - Número: {self.numero_conta}, Saldo: {self.saldo}"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            return True
        else:
            print("\nSaldo insuficiente para realizar o saque.")
            return False
