from random import randint
from time import sleep
print('\033[1:33m-=-\033[m' * 19)
print(f'\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[1:33m-=-\033[m' * 19)
n = int(input('Em que número eu pensei? '))
pc = randint(0, 5)
print(f'\033[1:35mPROCESSANDO...\033[m')
sleep(2)
if pc == n:
    print(f'\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')

else:
    print(f'\033[31mGANHEI!! Eu pensei no número {pc} e não no {n}!')
