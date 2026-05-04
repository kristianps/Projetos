import math

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3
media= math.ceil(media)
# Aqui outra forma de arrendondar:
# media = round(media, 1)

print("A media do aluno é: ", media)

# se a media for maior que sete, está aprovado
if media >= 0 and media <= 5.5:
    print("Reprovado")

elif media > 5.5 and media <= 6.5:
    print("Recuperação")

elif media > 6.5 and media <= 10:
    print("Aprovado")

else:
    print("Número não condiz com uma nota de 0 a 10")

    