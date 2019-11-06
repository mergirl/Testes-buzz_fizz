def solucao(n):
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0 and n % 5 == 0:
        return "buzz-fizz"
    return n
