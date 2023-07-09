a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos acima, \033[32mPODEM\033[m formar um triângulo!')
else:
    print(f'Os segmentos acima, \033[31mNÃO PODEM\033[m formar um triângulo! ')
