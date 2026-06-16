class Produto:
    def __init__(self, nome: str, preco: float, setor: str):
        self.nome = nome
        self.preco = preco
        self.setor = setor
        
    def exibir(self):
        print(f"Nome do produto: {self.nome} | Preço: R${self.preco} | Setor: {self.setor}")
        
def exibir_menu():
    print("\n====================")
    print("1 - Cadastrar Produto")
    print("2 - Calcular Total")
    print("3 - Filtrar por setor") 
    print("0 - Sair")
    print("====================")

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    setor = (input("Digite  setor do produto: "))
    produto = Produto(nome, preco, setor)
    carrinho.append(produto)

def exibir_produtos_e_total():
    if not carrinho:
        print("Não há produtos cadastrados!")
        print("Carrinho: R$ 00.00")
        return
    total = 0 
    for produto in carrinho:
        produto.exibir()
        total += produto.preco
    print(f"Total do carrinho: R${total}")

def filtrar_por_setor():
    setor = input("Digite o setor para filtrar: ")
    for codigo_produto, produto in enumerate(carrinho, start=1):
        if setor == produto.setor:
            print(f"Código produto: {codigo_produto}")
            produto.exibir()

carrinho = []
while True:
    exibir_menu()
    opcao = input("Escolha uma opcão: ")

    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        exibir_produtos_e_total()
    elif opcao == "3":
        filtrar_por_setor()
    else:
        print("Opção Inválida, Tente novamente.")