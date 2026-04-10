def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("O valor deve ser um inteiro.")
    if n < 0:
        raise ValueError("O valor deve ser maior que 0.")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

valor = int(input('Insira um inteiro maior que 0: '))
print(fibonacci(valor))
