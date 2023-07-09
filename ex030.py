n = int(input('\033[35mMe diga um número qualquer?\033[m '))

if n % 2 == 0:
    print(f'O número {n} é \033[31mPAR\033[m.')
else:
    print(f'O número {n} é \033[34mIMPAR\033[m.')
