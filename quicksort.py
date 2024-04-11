

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        metade_array = len(array) // 2
        pivo = array[metade_array]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([10, 5, 2, 3, 5, 7, 8, 6, 6, 100]))
