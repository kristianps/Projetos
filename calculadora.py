while True:
    menu = """
    --------CALCULADORA-------
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (*)
    4 - Divisão (\)
    0 - Sair
    """
    print(menu)
    escolha = input("Digite a opção: ")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    if escolha == "1":
        total = n1 + n2
        print (f" Sua conta de soma deu: {total}")   

    elif escolha == "2":
        total2 = n1 - n2
        print (f"Sua conta de subtração deu: {total2}")

    elif escolha == "3":
        total3 = n1 * n2
        print (f"Sua conta de multiplicação deu: {total3}")

    elif escolha == "4":
        total4 = n1 / n2
        print(f"Sua conta de divisão deu: {total4}")

    elif escolha == "0":
        exit

    else:
        print ("Opção Inválida!")
    break
    