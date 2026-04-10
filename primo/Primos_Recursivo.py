def primo(numero: int, divisor = 3):
    if numero < 2:
        return False
    elif numero == 2 or numero == 3:
        return True
    if numero % divisor == 0:
       return False
    if divisor * divisor > numero:
        return True

    return primo(numero, divisor+2)

def primos_n(n, novo = 3):
    if novo == 3:
        if not isinstance(n, int):
            raise TypeError("O número deve ser um inteiro.")
        if n <= 1:
            raise ValueError('O número deve ser maior que 1.')
    
    
    if novo > n:
        return sorted([2]) 

    if primo(novo) == True:
        return [novo] + primos_n(n, novo + 2)
    else:
        return primos_n(n, novo + 2)

inp = int(input('digite um numero inteiro e maior que 1: '))
print(primos_n(inp))
