menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

depositos = ""
saques = ""


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = int(input("Insira o valor do depósito:"))
        if deposito > 0:
            saldo += deposito
            depositos += "Deposito: " + str(deposito) + "\n"
            print("Depósito realizado com sucesso")
        else: print("Valor inválido")

    
    elif opcao == "s":
        print("Saque")
        if numero_saques > 2:
            print("Limite de saques já foi atingido")
        else:
            saque = int(input("Insira o valor do saque:"))
            if saque > 500:
                print("Erro. O limite máximo de saque é 500 reais")
            elif saque > saldo:
                print("Saldo insuficiente")
            else:
                numero_saques += 1
                saldo -= saque
                saques += "Saque: " + str(saque) + "\n"
                print("Saque realizado com sucesso")

    elif opcao == "e":
        extrato += depositos + saques
        print(f"Extrato: \n{extrato} \nSaldo atual da conta: R$ {saldo}")

    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

    
