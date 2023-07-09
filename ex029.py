# Variáveis
velo = float(input('\033[1mQual é a velocidade atual do carro? '))
multa = (velo - 80) * 7
# lógica
if velo <= 80:
    print(f'\033[33mTenha um bom dia! Dirija com segurança!')
else:
    print(f'\033[31mMULTADO! Você excedeu o limite permitido que é de \033[32m80Km/h\033[m\n'
          f'Você deve pagar uma multa de \033[35mR${multa:.2f}!\n'
          f'\033[34mDirija com mais segurança!')
