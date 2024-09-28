menu = """
<<<Sistema Bancário>>>
[d] Depositar
[s] Sacar
[t] Transferir
[p] Pagar Conta
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas_pagas = ""

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

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
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def transferir(saldo, extrato):
    valor = float(input("Informe o valor da transferência: "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f"Transferência: R$ {valor:.2f}\n"
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
    else:
        print("Operação falhou! Saldo insuficiente ou valor inválido.")
    return saldo, extrato

def pagar_conta(saldo, extrato, contas_pagas):
    valor = float(input("Informe o valor da conta: "))
    descricao = input("Informe a descrição da conta: ")
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f"Pagamento: {descricao} - R$ {valor:.2f}\n"
        contas_pagas += f"{descricao}: R$ {valor:.2f}\n"
        print(f"Conta '{descricao}' paga com sucesso!")
    else:
        print("Operação falhou! Saldo insuficiente ou valor inválido.")
    
    return saldo, extrato, contas_pagas

def exibir_extrato(saldo, extrato, contas_pagas):
    print("\n================ EXTRATO ================")
    if not extrato and not contas_pagas:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        if contas_pagas:
            print("\nContas pagas:\n", contas_pagas)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques)

    elif opcao == "t":
        saldo, extrato = transferir(saldo, extrato)

    elif opcao == "p":
        saldo, extrato, contas_pagas = pagar_conta(saldo, extrato, contas_pagas)

    elif opcao == "e":
        exibir_extrato(saldo, extrato, contas_pagas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
