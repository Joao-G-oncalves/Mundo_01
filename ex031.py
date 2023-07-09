distancia = float(input('Qual é a distância da sua viagem? '))
preco1 = distancia * 0.50
preco2 = distancia * 0.45
print(f'Você está prestes a começar uma viagem de {distancia:.0f}Km.')
if distancia > 200:
    print(f'E o preço da sua passagem será de \033[35mR${preco2:.2f}\033[m!')
else:
    print(f'E o preço da sua passagem será de \033[35mR${preco1:.2f}\033[m!')
