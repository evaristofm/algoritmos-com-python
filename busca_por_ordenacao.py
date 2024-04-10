
def buscaMenor(arr: list):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr: list):
    novoArr = list()
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
