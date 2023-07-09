salario = float(input('Qual é o salário do Funcionário? R$'))
print(f'Um funcionário que ganhava \033[31mR${salario:.2f}\033[m, com aumento de 15%, passa a receber '
      f'\033[32mR${salario + (salario * 0.15):.2f}\033[m!')
