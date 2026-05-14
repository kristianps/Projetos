contador = 0
# While true serve para repetir infinitamente.
while True:
#int serve para reconhecer somente números, já o input, serve para você ser a pessoa que irá escrever, e não a máquina.
    numero = int(input("Digite o número desejado: "))
    print("DIGITE '0' PARA SAIR")
#dois "=" serve para ser um comparador, não um "igual".
    if numero == 0:
        print(f"Você digitou {contador} vezes. ")
        break
#break para sair do loop.
    contador += 1