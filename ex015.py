dias = int(input('Quantos dias alugados? '))
vd = dias * 60
km = float(input('Quantos Km rodados? '))
vkm = km * 0.15
print(f'Você ficou com carro por \033[1:31m{dias} dias\033[m e andou \033[1:31m{km} Km\033[m!')
print(f'O total a pagar é de \033[1:32mR${vd + vkm:.2f}\033[m!')
