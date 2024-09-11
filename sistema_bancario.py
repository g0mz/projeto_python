menu = """

[d] Depósito
[s] Saque
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("\nOperação: Depósito\n")
        
        valor_depositado = float(input("Insira o valor do depósito: \n"))

        if valor_depositado > 0: 

            saldo += valor_depositado
            print(f"\nValor de R$ {valor_depositado} depositado com sucesso!")
            extrato += f"Depósito: R$ {valor_depositado}\n"

        else: 
            print("\nValor inválido para depósito.")
        
    elif opcao == "s":
        print("\nOperação: Saque")

        saque = float(input("Insira o valor do saque: \n"))
        numero_saques += 1

        if numero_saques <= LIMITE_SAQUES:
            

            if (saque <= 500) and (saque > 0):
                
                if saque <= saldo:
                    saldo -= saque
                    print(f"\nSaque no valor de R$ {saque} realizado com sucesso!")
                    extrato += f"Saque: R$ {saque}\n"
                else:
                    print("\nSaldo insuficiente para saque.")

            else: 
                print("\nValor de saque acima do permitido.")
    
        else:
            print("\nNúmero limite de saques diários atingido.")

    elif opcao == "e":
        print("\n============Extrato============\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo}")
        print(f"Número de saques realizados: {numero_saques}\n")
        print("===============================\n")


    elif opcao == "x":
        print("\nO sistema bancário será encerrado.")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente.\n")
