frutas = ["maça","banana", "manga", "abacaxi", "ameixa"]

fruta_favorita = input("Digite sua fruta favorita:")

if fruta_favorita not in frutas:
    print("Sua fruta favorita não está na lista!")
    exit()

# Para cada posição (índice) e fruta na lista numerada
for posição, fruta in enumerate(frutas):
    posiçãoFruta = posição
    # Faça isso:
    # Se a fruta dessa iteração é igual a fruta favorita
    if fruta == fruta_favorita:
        # Salva numa nova variável a posição dessa iteração

        posição_fruta_favorita = posição
        # Quebra o 'for' (faz ele parar)
        break

#Saída do algoritmo (print)
print(f"Sua fruta favorita está no índice {posição} ")