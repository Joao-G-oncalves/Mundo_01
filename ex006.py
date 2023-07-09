from math import sqrt
n = int(input('\033[32mDigite um número: '))
print(f'\033[34mO dobro de {n} vale {n*2}.\n'
      f'\033[31mO triplo de {n} vale {n*3}.\n'
      f'\033[33mA raiz quadrada de {n} é igual a {sqrt(n):.2f}.')
