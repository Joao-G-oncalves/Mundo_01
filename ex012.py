preco = float(input('Qual é o preço do produto? R$'))
print(f'O produto que custava \033[31mR${preco:.2f}\033[m, na promoção com desconto de 5%, vai custar '
      f'\033[32mR${preco - (preco * 0.05):.2f}\033[m!')
