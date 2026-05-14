idade = -1
tentativas = 0

while idade <0 or idade > 120:
    idade = int(input("Digite uma idade válida de 0 a 120:"))

    if idade < 0 or idade > 120:
        print("Idade Inválida! Tente novamente.")

print(f"Obrigado! A idade digitada foi: {idade}")