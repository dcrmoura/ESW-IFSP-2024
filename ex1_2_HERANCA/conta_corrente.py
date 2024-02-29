from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo, limite_cheque_especial):
        super().__init__(numero_conta, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def detalhes_conta(self):
        return f"\nConta Corrente - Número: {self.numero_conta}, Saldo: {self.saldo}, Limite Cheque Especial: {self.limite_cheque_especial}"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite_cheque_especial:
            self.saldo -= valor
            return True
        else:
            print("\nSaldo insuficiente para realizar o saque.")
            return False
