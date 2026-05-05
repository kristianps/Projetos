Valor = float(input("D1igite o valor do pedido R$:"))

"""
Regras de negócios:
*se a venda for 100 reais, de 5% de desonto
*se a venda for entre 101 a 299 reais, de 10% de desconto
*se a venda for maior que 300 reais, de 15% desconto

"""

if Valor <= 100:
    desconto = 0.95

elif Valor > 100 and Valor <= 299.99:
    desconto = 0.90
    
else:
    desconto = 0.85


total = Valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual,0)

print("Valor total foi de: R$", Valor)
print("")
print("O desconto foi aplicado: R$", total)
print("")
print (f" Sua compra deu R${Valor}. Você ganhou {descontoPercentual}%"
f" de desconto. O total agora é R$ {total}.")
print("")