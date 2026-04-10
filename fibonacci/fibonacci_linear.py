def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("O valor deve ser um inteiro.")
    if n <= 0:
        raise ValueError("O valor deve ser maior que 0.")
    if n == 1:
        return [0]

    lista = [0,1]

    for a in range(n-1):
        lista.append(lista[-1] + lista[-2])
    return lista

valor = int(input('Insira um inteiro maior que 0: '))
print(fibonacci(valor))
