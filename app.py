# Trabalho de informática, professora Nadya
# Programa de listas de tarefas em Python
# Gabriel Victor, Juan Pablo, Kevin Gomes


import os

lista = []

def exibir_nome_do_programa():
    print("Boas Vindas a lista\n")


def mostrando_opções():
    print("Escolha uma opção abaixo: ")
    print("1- Exibir lista")
    print("2- Listar novo item")
    print("3- Remover itens")
    print("4- Sair")


# Exibe a lista para o usuário, caso vazia, não é exibida
def listar_itens():
    if not lista:
        print("Nenhum item por aqui.")
    else:
        print("Sua lista: ")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")


# Adiciona novos itens na lista
def novos_itens():
    item = input("Digite o item a ser adicionado: ")
    lista.append(item)
    print(f"{item} adicionado(a) com sucesso!")


# Antes do usuário remover algum item da lista, o programa exibe a lista para o usuário selecionar o que deseja remover
def remover_itens():
    if not lista:
        print("A lista está vazia. Não há itens para remover.")
        return

    listar_itens()
    try:
        numero = int(input("Digite o número do item a ser removido: "))
        if 0 < numero <= len(lista):
            item_removido = lista.pop(numero - 1)
            print(f"Item {item_removido} foi removido com sucesso!")
        else:
            print("Esse item não existe na lista!")
    except ValueError:
        print("Digite um número válido.")


# Fecha o programa
def sair():
    os.system("cls" if os.name == "nt" else "clear")
    print("Encerrando programa...")


# Caso o usuário não digite algum certo, é exibida uma mensagem de erro
def erro():
    print("ERRO de opção não encontrada")

def exibir_subtitulo(texto):
    os.system("cls" if os.name == "nt" else "clear")
    print(texto)
    print()


# Quando o usuário selecionar uma opção, as funções acima serão acionadas
def escolhendo_opção():

    try:

        opçao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção: {opçao_escolhida}\n")

        if opçao_escolhida == 1:
            listar_itens()
        elif opçao_escolhida == 2:
            novos_itens()
        elif opçao_escolhida == 3:
            remover_itens()
        elif opçao_escolhida == 4:
            sair()
            exit()
        else:
            erro()
    except ValueError:
        erro()

# Para que o programa continue rodando, até que o usuário escolha parar
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        exibir_nome_do_programa()
        mostrando_opções()
        escolhendo_opção()
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()