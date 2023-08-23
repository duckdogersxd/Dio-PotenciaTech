LIMITE_SAQUE = 500
AGENCIA = "0001"
usuarios_cadastrados = {}
num_conta_seq = 1


class usuario:
    def __init__(self, nome, dt_nasc, cpf, end):
        self.nome = nome
        self.data_nascimento = dt_nasc
        self.cpf = cpf
        self.endereco = end
        self.contas = []

    def adicionarConta(self, conta):
        self.contas.append(conta)

    def exibirContas(self):
        for i in self.contas:
            linha = f"""\
                        Agência:\t{i.agencia}
                        C/C:\t\t{i.num}
                        Titular:\t{self.nome}
                    """


class conta:
    def __init__(self, saldo=0):
        global num_conta_seq
        self.saques_dia = 0
        self.agencia = AGENCIA
        self.num = num_conta_seq
        num_conta_seq += 1
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


menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [lu]\tListar usuários
    [nu]\tNovo usuário
    [q]\tSair
    => """
opcao = input(menu)

while opcao != "q":

    if opcao == "d":
        cpf = input("Informe o CPF (somente número): ")
        if cpf in usuarios_cadastrados:
            print(f"Usuário: {usuarios_cadastrados[cpf].nome}")
            contas_usu = usuarios_cadastrados[cpf].contas
            for i in range(len(contas_usu)):
                print(f"{i} - Número da Conta:{contas_usu[i].num} Agência{contas_usu[i].agencia}")
            selecao = int(input("Selecione a conta de acordo com o número referente a ela:"))
            valor = float(input("Informe o valor do depósito: "))
            contas_usu[selecao].deposito(valor)

    elif opcao == "s":
        cpf = input("Informe o CPF (somente número): ")
        if cpf in usuarios_cadastrados:
            print(f"Usuário: {usuarios_cadastrados[cpf].nome}")
            contas_usu = usuarios_cadastrados[cpf].contas
            for i in range(len(contas_usu)):
                print(f"{i} - Número da Conta:{contas_usu[i].num} Agência{contas_usu[i].agencia}")
            selecao = int(input("Selecione a conta de acordo com o número referente a ela:"))
            valor = float(input("Informe o valor do saque: "))
            contas_usu[selecao].saque(valor)

    elif opcao == "e":
        cpf = input("Informe o CPF (somente número): ")
        if cpf in usuarios_cadastrados:
            print(f"Usuário: {usuarios_cadastrados[cpf].nome}")
            contas_usu = usuarios_cadastrados[cpf].contas
            for i in range(len(contas_usu)):
                print(f"{i} - Número da Conta:{contas_usu[i].num} Agência{contas_usu[i].agencia}")
            selecao = int(input("Selecione a conta de acordo com o número referente a ela:"))
            contas_usu[selecao].exibirExtrato()

    elif opcao == "nu":
        cpf = input("Informe o CPF (somente número): ")
        if cpf in usuarios_cadastrados:
            print("Já existe usuário com esse CPF!")
        else:
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            usuarios_cadastrados[cpf] = usuario(nome, data_nascimento, cpf, endereco)
            print("=== Usuário criado com sucesso! ===")
    elif opcao == "nc":
        cpf = input("Informe o CPF do usuário: ")

        if cpf in usuarios_cadastrados:
            conta_aux = conta()
            usuarios_cadastrados[cpf].adicionarConta(conta_aux)
            print("\n=== Conta criada com sucesso! ===")
            print(f"Agencia{conta_aux.agencia} Número{conta_aux.num}")

    elif opcao == "lc":
        cpf = input("Informe o CPF do usuário: ")
        if usuarios_cadastrados[cpf] is None:
            print("Usuário não encontrado!")
        else:
            for usuarios in usuarios_cadastrados.values():
                print(f"Usuário: {usuarios.nome}")
                for contas in usuarios.contas:
                    print(f"Número:{contas.num} Agência:{contas.agencia}")
    elif opcao == "lu":
        for usuarios in usuarios_cadastrados.values():
            print(f"Nome:{usuarios.nome}  Cpf:{usuarios.cpf}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    opcao = input(menu)
