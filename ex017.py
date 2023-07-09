# PRIMEIRA FORMA DE FAZER
# from math import hypot
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# print(f'A hipotenusa vai medir \033[4m\033[3:34m{hypot(co, ca):.2f}\033[m!')

# SEGUNDA FORMA DE FAZER
from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# h = (co ** 2 + ca ** 2) ** (1/2) << FORMA DE FAZER SEM USAR O MATH
h = sqrt(co ** 2 + ca ** 2)
print(f'A hipotenusa vai medir {h:.2f}')
