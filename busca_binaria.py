minha_lista = [1, 3, 5, 7, 9]


def pesquisa_binaria(lista: list, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2)  # metada da lista
        chute = lista[meio]

        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))
