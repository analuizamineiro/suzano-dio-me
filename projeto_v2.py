def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [user] Cadastrar Usuário
    [cc] Cadastrar Conta Corrente
    [q] Sair

    => """


# keyword only
def saque(*, saldo, valor, extrato, limite, limite_saques, numero_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Operação realizada. Saque de R$ {valor:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

# position only
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Operação realizada. Depósito de R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# keyword only (extrato) e position only (saldo)
def visualizar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(lista_usuarios):

    nome = str(input("Insira seu nome completo: "))
    data_nascimento = str(input("Insira sua data de nascimento no formato DD-MM-YYYY: "))
    cpf = int(input("Insira seu CPF (Use apenas números): "))
    endereco = str(input("Insira seu endereço no fomato logradouro, nro - bairro - cidade/ sigla estado: "))
    usuario = {
        "nome": nome,
        "data de nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco}
    
    # Verifica se o usuário ja existe
    if any(u["cpf"] == usuario["cpf"] for u in lista_usuarios):
        print("Usuário com este CPF já existe")

    else:
        lista_usuarios.append(usuario)
        print(f"Usuário criado! \n{lista_usuarios[-1]}")

    return lista_usuarios


def criar_conta(lista_contas, lista_usuarios, agencia, numero_conta):
    cpf = int(input("Insira seu CPF (Use apenas números): "))

    usuario_encontrado = None
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta += 1
        conta_info = {
            "usuário": usuario_encontrado["nome"],
            "agência": agencia,
            "número da conta": numero_conta
        }
        lista_contas.append(conta_info)
        print(f"Conta corrente criada! \n{lista_contas[-1]}")

    else:
        print("Este CPF não está cadastrado.")

    return lista_contas, numero_conta 



def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 0

    lista_usuarios = []
    lista_contas = []

    while True:
        opcao = input(menu())

        if opcao == 'd':
            print("Você escolheu a Operação Depósito.")
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            print("Você escolheu a Operação Saque.")
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques
            )

        elif opcao == 'e':
            print("Você escolheu a Operação Visualizar Extrato.")
            visualizar_extrato(saldo, extrato=extrato)


        elif opcao == 'user':
            print("Você escolheu a Operação Criar Novo Usuário.")
            lista_usuarios = criar_usuario(lista_usuarios)


        elif opcao == 'cc':
            print("Você escolheu a Operação Criar Conta Corrente.")

            lista_contas, numero_conta = criar_conta(lista_contas, lista_usuarios, AGENCIA, numero_conta)
    

        elif opcao == 'q':
            print("Saindo do sistema.")
            break

    
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()