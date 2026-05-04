print("")
nota = float(input("Digite a primeira nota do aluno: "))
print("")
if 0 <= nota <= 6:
    print("reprovado")

elif 6 <= nota <= 7:
    print("Recuperação")

elif 7<= nota <=10:
    print("Aprovado")

else: print("Não condiz com 0 a 10")
print("")