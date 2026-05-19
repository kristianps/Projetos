while True:
    try:
        numero = int(input("Digite um número: "))
        break  # sai do loop se der certo

    except ValueError:
        print("Erro: digite apenas números inteiros.")

if numero > 0:
    print("Esse número é positivo")

elif numero < 0:
    print("Esse número é negativo")

elif numero == 0:
    print ("Esse número é igual a 0")