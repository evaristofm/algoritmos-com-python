
def regressiva(num: int):
    print(num)
    if num <= 1:  # Caso base: é quando a função deve parar
        return
    regressiva(num - 1)  # Caso recursivo: É quando uma função chama a si novamente


regressiva(5)
