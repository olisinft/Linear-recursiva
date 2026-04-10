def primo(numero: int, divisor = 3):
    if numero < 2:
        return False
    if numero == 2 or numero == 3:
        return True
    while divisor * divisor <= numero:
        if  numero % divisor == 0:
            return False
        divisor += 2
    return True

def primos_n(n):
    if not isinstance(n, int):
        raise TypeError("O número deve ser um número inteiro.")
    if n <= 1:
        raise ValueError("O número deve ser maior que 1.")
    
    lista = [2]
    for i in range(3, n+1, 2):
        if primo(i) == True:
            lista.append(i)
    return (lista)

inp = int(input('digite um numero inteiro e maior que 1: '))
print(primos_n(inp))
