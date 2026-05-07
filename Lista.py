produtos = ["MacBook", "Celular", "Computador", "Teclado", "Mouse"]
preços = [150.00, 100.00, 200.00, 50.00, 250.00]
print ("")
print("Lista Dos Produtos:", produtos) # imprime "Todos da lista"
print("Produto:", produtos[0]) # imprime "MacBook"
print("Protudo:", produtos[4]) # imprime "Mouse"
print("")
# Para exibir o valor do produto que deseja:
print(f"O Produto {produtos[0]} Custa: R${preços[0]}")
print("")
# Para remover o preço ou o produto:
produtos.remove(produtos[-1])
preços.remove(preços[-1])
print("")
# Para somar o preço de todos os produtos:
total = sum(preços)
print(f"O Total Deu R${total:.2f}")

# Lógica Condicional if/else para desconto:
if total < 500:
    exit()

# Caso, seguir uma sequência diferente dos total acima^, fazer desta outra forma:
else:
    desconto = 0.95
    total = total * desconto
    print(f"O Total Agora Com Desconto é de R%{total:.2f}")
print("")

