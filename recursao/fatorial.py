

def fat(x: int):
    if x == 1:
        return 1
    return x * fat(x - 1)


fat(5)
