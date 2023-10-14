"""
Upgrades realizados na v2 desse sistema bancário:
> Criado Funções separadas para saque, depósito e extrato
> Adicionado novas funções:
    - Cadastro de usuários (clientes)
    - Cadastro de contas bancárias
    - Listagem de contas
    - Filtro de usuários

> Em cada função, foi implementado uma regra diferente na passagem de argumentos
> Argumentos < keyword only / positional only >
"""

import textwrap

def Depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito < 0:
        print("Insira um valor válido\n") 
    else:
        saldo += valor_deposito
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"R$ {valor_deposito} Depositado com sucesso!")
    return saldo, extrato

def Sacar (*, saldo, valor_saque, extrato, limite, num_saque):
    if valor_saque < 0:
        print("Insira um valor válido\n")
    elif saldo >= valor_saque <= limite and num_saque < 3:
        saldo -= valor_saque
        num_saque += 1
        extrato.append(f"Saque: R${valor_saque:.2f}")
        print(f"Saque de R${valor_saque} realizado com sucesso!\n")
    elif valor_saque > limite:
        print("Valor solicitado excede o limite.\n")
    else:
        print("Saldo insuficiente.\n")        

    return saldo, extrato, num_saque

def extratto (saldo, /, extrato):
    print("""========== Extrato ==========""")
    extrato_formatado = [transacao for transacao in extrato]
    extrato_string = "\n".join(extrato_formatado)
    print(extrato_string)
    print(f"\nSaldo: R${saldo}")
    print("""=============================""")

    return saldo, extrato

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("\n Já existe usuário com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    dt_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro - nº - bairro - cidade/Estado): ")
    
    usuarios.append({"nome": nome, "dt_nascimento": dt_nascimento, "cpf": cpf, "endereco":endereco})
    print("Usuário criado com sucesso!!")

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input ("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("\n Conta criada com sucesso!")
        return {"agencia": agencia,  "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!!")

def lista (contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print ("="*20)
        print (textwrap.dedent(linha))
    else:
        print("\n Lista de Contas está vazia")

menu="""
:::::::::::::: MENU :::::::::::::::
 [1] Depositar   [5] Listar Contas
 [2] Sacar       [6] Novo Usuário
 [3] Extrato     [7] Sair
 [4] Nova Conta
:::::::::::::::::::::::::::::::::::
    """
AGENCIA = "0001"
usuarios = []
num_saque = 0
limite = 500
extrato = []
contas = []
saldo = 0


while True:
    opcao = input(menu)
    if opcao == "1":
        valor_deposito = float(input("Informe o valor que deseja depositar: "))
        saldo, extrato = Depositar (saldo, valor_deposito, extrato)

    elif opcao == "2":
        if num_saque >= 3:
            print("Número máximo de saques excedido!\n")
            break
        else:
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato, num_saque = Sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                num_saque= num_saque
             )

    elif opcao == "3":
        extratto (saldo, extrato=extrato)

    elif opcao == "4":
        numero_conta = len (contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios) 

        if conta:
            contas.append(conta)

    elif opcao == "5":
        lista(contas)

    elif opcao == "6":
        criar_usuario(usuarios)

    elif opcao == "7":
        break
    else:
        print("Operação inválida, selecione novamente a opção desejada!")
