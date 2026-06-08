def exibir_menu():
    print("\n========================")
    print("Conta Bancária: ")
    print("1 - Depositar.")
    print("2 - Sacar.")
    print("3 - Ver saldo.")
    print("0 - Para sair")
    print("==========================")

def depositar(saldo):
    valor = float(input("Digite um valor para depósito: "))

    saldo = saldo + valor
    print(f"Depósito de {valor:.2f} realizado!")
    return saldo

def sacar(saldo):
    saque = float(input("Digite um valor para saque: "))

    if saque > saldo:
        print("Saldo insuficiente para saque.")
        return saldo
    
    saldo = saldo - saque
    print(f"Saque de {saque:.2f} realizado!")
    return saldo

def ver_saldo(saldo):
    print(f"Saldo atual: {saldo:.2f}")

saldo = 0.0
while True:
    exibir_menu()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        saldo = depositar(saldo)
    elif opcao == "2":
        saldo = sacar(saldo)
    elif opcao == "3":
        ver_saldo(saldo)
    else:
        print("Opção Inválida, Tente novamente.")