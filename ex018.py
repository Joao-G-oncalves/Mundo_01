from math import sin, cos, tan, radians
angulo = float(input('\033[33mDigite o ângulo que você deseja: '))

print(f'\033[31mO ângulo de {angulo} tem o Seno de {sin(radians(angulo)):.2f}; \n'
      f'\033[32mO ângulo de {angulo} tem o Cosseno de {cos(radians(angulo)):.2f};\n'
      f'\033[34mO ângulo de {angulo} tem a Tangente de {tan(radians(angulo)):.2f}.')
