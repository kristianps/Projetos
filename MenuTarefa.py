def exibir_menu():
    print("\n========================")
    print("Menu: ")
    print("1 - Para adicionar")
    print("2 - Para listar")
    print("3 - Para Remover")
    print("0 - Para sair")
    print("==========================")

def adicionar_tarefas(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
            print("Não há tarefas registradas!")
    else:
        for posicao_tarefa, tarefa in enumerate(tarefas, start=1):
            print(f"{posicao_tarefa} - {tarefa}")

def remover_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas registradas para remover.")
    else:
        tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        tarefa = tarefa - 1
        tarefa_removida = tarefas.pop(tarefa)
        print(f"Tarefa removida: {tarefa_removida}")
 
tarefas = []

while True:
    exibir_menu()
    opcao = input("Esolha uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        tarefas.append
        adicionar_tarefas(tarefas)

    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        remover_tarefa(tarefas)

    else:
        print("Opção inválida!")