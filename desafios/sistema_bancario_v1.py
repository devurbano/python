menu="""
:::::::::::: MENU :::::::::::
 [1] Depositar   [3] Extrato
 [2] Sacar       [4] Sair
:::::::::::::::::::::::::::::
    """

limite = 500
extrato = []
saldo = 0
num_saque = 0

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor que deseja depositar: "))
        if valor_deposito < 0:
            print("Insira um valor válido\n")
        else:
            saldo += valor_deposito
            extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
            print(f"R$ {valor_deposito} Depositado com sucesso!")
            
    elif opcao == "2":
        valor_saque = float(input("Informe o valor que deseja sacar: "))
        if valor_saque < 0:
            print("Insira um valor válido\n")
        elif saldo >= valor_saque <=limite and num_saque <3:
            saldo -= valor_saque
            num_saque += 1
            extrato.append(f"Saque: R${valor_saque:.2f}")
            print(f"Saque de R${valor_saque} realizado com sucesso!\n")
        elif valor_saque > limite:
            print("Valor solicitado excede o limite.\n")
        elif num_saque >= 3:
            print("Número máximo de saques excedido.\n")
            break
        else:
            print("Saldo insuficiente.\n")         
            
    elif opcao == "3":
        print("""========== Extrato ==========""")
        extrato_formatado = [transacao for transacao in extrato]
        extrato_string = "\n".join(extrato_formatado)
        print(extrato_string)
        print(f"\nSaldo: R${saldo}")
        print("""=============================""")
      
    elif opcao == "4":
        break
        
    else:
        print("Opção inválida")
