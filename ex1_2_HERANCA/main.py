from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from conta_investimento import ContaInvestimento

def menu():
    print("\n\t# Sistema Bancário #")
    print("\nSelecione uma opção:")
    print("1. Abrir conta")
    print("2. Visualizar informações das contas de um cliente")
    print("0. Sair")

def abrir_conta(clientes):
    codigo = input("\nDigite o código do cliente: ")
    nome = input("Digite o nome do cliente: ")

    cliente = Cliente(codigo, nome)
    clientes.append(cliente)

    print(f"\nCliente código {codigo} criado com sucesso!\n")
    return cliente

def criar_conta(cliente):
    while True:
        print("\nSelecione o tipo de conta:")
        print("1. Conta Corrente")
        print("2. Conta Poupança")
        print("3. Conta de Investimento")
        print("0. Encerrar abertura de contas para este cliente")

        opcao_conta = input("\nDigite o número da opção desejada: ")

        if opcao_conta == "0":
            break

        elif opcao_conta == "1":
            numero_conta = input("\nDigite o número da conta corrente: ")
            saldo = float(input("Digite o saldo inicial: "))
            limite = float(input("Digite o limite do cheque especial: "))
            conta_corrente = ContaCorrente(numero_conta, saldo, limite)
            cliente.adicionar_conta(conta_corrente)
            print("Conta corrente criada com sucesso!\n")

        elif opcao_conta == "2":
            numero_conta = input("\nDigite o número da conta poupança: ")
            saldo = float(input("Digite o saldo inicial: "))
            conta_poupanca = ContaPoupanca(numero_conta, saldo)
            cliente.adicionar_conta(conta_poupanca)
            print("Conta poupança criada com sucesso!\n")

        elif opcao_conta == "3":
            numero_conta = input("\nDigite o número da conta de investimento: ")
            saldo = float(input("Digite o saldo inicial: "))
            conta_investimento = ContaInvestimento(numero_conta, saldo)
            cliente.adicionar_conta(conta_investimento)
            print("Conta de investimento criada com sucesso!\n")

def buscar_cliente(codigo, clientes):
    for cliente in clientes:
        if cliente.nome == codigo:
            return cliente
    return None

if __name__ == "__main__":
    clientes = []

    while True:
        menu()
        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == "1":
            cliente = abrir_conta(clientes)
            criar_conta(cliente)

            # Após criar a primeira conta para o cliente, perguntar se deseja adicionar outra conta
            resposta = input("\nDeseja adicionar outra conta para este cliente? (s/n): ")
            if resposta.lower() != 's':
                continue  # Se a resposta não for 's', volta para o menu inicial

        elif opcao == "2":
            codigo_cliente = input("\nDigite o código do cliente para visualizar as contas: ")
            cliente_encontrado = buscar_cliente(codigo_cliente, clientes)

            if cliente_encontrado:
                cliente_encontrado.listar_contas()
            else:
                print("\nCliente não encontrado.\n")

        elif opcao == "0":
            print("\n\nEncerrando o programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")
