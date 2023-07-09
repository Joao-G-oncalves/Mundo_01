# PRIMEIRA FORMA DE FAZER
# n = float(input('Digite um valor: '))
# valor = n // 1
# resto = n % 1
# print(f'O valor digitado foi {n} e a sua porção inteira é {valor:.0f}')

# SEGUNDA FORMA DE FAZER
# n = float(input('Digite um valor: '))
# print(f'O valor digitado foi {n} e a sua porção inteira é {int(n)}!')

# TERCEIRA FORMA DE FAZER
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)}')
