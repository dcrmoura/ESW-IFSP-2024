class Cliente:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        if not self.contas:
            print(f"{self.nome} não possui contas.")
        else:
            print(f"Contas de {self.nome}:")
            for conta in self.contas:
                print(conta.detalhes_conta())
                print()
