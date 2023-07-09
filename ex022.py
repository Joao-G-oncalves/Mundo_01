from time import sleep
frase = str(input('Digite seu nome completo: ')).strip()
print(f'\033[31mAnalisando seu nome...\033[m')
separado = frase.split()
sleep(2)
print(f'Seu nome em maiúsculas é {frase.upper()}!')
print(f'Seu nome em minúsculas é {frase.lower()}!')
print(f'Seu nome tem ao todo {len(frase) - frase.count(" ")} letras! ')
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras!')
