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

def listar_itens():
    if not lista:
        print("Nenhum item por aqui.")
    else:
        print("Sua lista: ")
        for i, lista in enumerate(lista, start=1):
            print(f"{i}. {lista}")

def novos_itens(lista):
    lista.append(lista)
    print(f"{lista} adicionado(a) com sucesso!")

def remover_itens(numero):
    if 0 < numero <= len(lista):
        item_removido = lista.pop(numero - 1)
        print(f"Item {item_removido} foi removido com sucesso!")
    else:
        print("Esse item na existe na lista!")

def sair():
    os.system("cls")
    print("Encerrando programa...")
    exibir_subtitulo("Encerrando o programa")

def erro():
    print("ERRO de opção não encontrada")

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

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
        else:
            erro()
    except:
        erro()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    mostrando_opções()
    escolhendo_opção()

if __name__ == "__main__":
    main()