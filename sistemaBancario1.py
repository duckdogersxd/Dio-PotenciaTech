LIMITE_SAQUE = 500


class conta:
    def __init__(self, saldo=0):
        self.saques_dia = 0
        if saldo > 0:
            self.extrato = [("d", saldo)]
            self.saldo = saldo
            print("Conta criada com sucesso e depósito realizado!")
        elif saldo == 0:
            self.saldo = saldo
            self.extrato = []
            print("Conta criada com sucesso!")
        else:
            print("Valor inicial da conta inválido!")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(("d", valor))
            print("Depósito realizado!")
        else:
            print("Valores Negativos não são válidos!")

    def saque(self, valor):
        if self.saques_dia >= 3:
            print("Número máximo de saques diários realizados!")
        elif valor > LIMITE_SAQUE:
            print("O valor solicitado ultrapassou o limite de saque!")
        elif valor <= 0:
            print("Valor inválido!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.saques_dia += 1
            self.extrato.append(("s", valor))

    def exibirExtrato(self):
        print("\n================ EXTRATO ================")
        if self.extrato == []:
            print("Não foram realizadas movimentações.")
        else:
            for i in self.extrato:
                if "d" == i[0]:
                    print(f"Depósito: R$ {i[1]:.2f}")
                elif "s" == i[0]:
                    print(f"Saque: R$ {i[1]:.2f}")
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
opcao = input(menu)

user = conta()
while opcao != "q":

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        user.deposito(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        user.saque(valor)

    elif opcao == "e":
        user.exibirExtrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    opcao = input(menu)
