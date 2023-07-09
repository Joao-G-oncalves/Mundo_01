nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
print(f'Muito prazer em te conhecer!\n'
      f'Seu primeiro nome é {primeiro[0]}\n'
      f'Seu último nome é {primeiro[len(primeiro)-1]}\n')
