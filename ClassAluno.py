class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def exibir(self):
        print(f"Aluno: {self.nome}, Nota: {self.nota}")

def exibir_menu():
    print("======================")
    print("1 - Cadastro de Alunos")
    print("2 - Exibir Notas")
    print("0 - Sair")
    print("======================")

def cadastrar_aluno():
    print("\nCADASTRANDO ALUNO....")
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)

    aluno.exibir()


alunos = []

cadastrar_aluno()
