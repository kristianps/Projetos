usuario_correto = "admin"
senha_correta = "1234"

while True:
    print("---------PAINEL DE LOGIN--------")
    usuario = (input("Digite o usúario: "))
    senha = int(input("Digite a senha: "))

    if usuario == usuario_correto and senha_correta:
        print("Acesso liberado!")
        break

    else:
        print("Acesso negado!")
    