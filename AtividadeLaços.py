produtos = ["Camisa","Casaco","Tênis","Calça", "Cueca"]
preços = [50.00, 80.00, 60.00, 70.00, 20.00]
quantidades = [2, 3, 4, 1, 6]
subtotais = []
#ANTES, FAÇA ASSIM PARA PEAR O PRODUTO E PREÇO DO PRODUTO:

print(f"O produto {produtos[0]} custa R$: {preços[0]}.")

for indice, produtos in enumerate(produtos):
    preço = preços[indice] # Pega o produto e preço e seleciona automaticamente consequentemente.
    quantidade = quantidades [indice]
    subtotal = quantidade * preço
    subtotais.append(subtotal)
  
    mensagem = f"""
    -----------------------------------------
    Produto: {produtos}
    Quantidade: {quantidade}
    Valor unitário: {preço}
    Subtotal: {subtotal}
    ------------------------------------------
    """
    print (mensagem)

print(f"O total da compra deu R$: {sum(subtotais)}")
