#29) Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre o novo salário, reajustado de acordo com tabela:
# - Até 3 anos de empresa: aumento de 3%
#- entre 3 e 10 anos: aumento de 12.5%
#- 10 anos ou mais: aumento de 20%

nome = input('Nome do funcionário: ')
salario = float(input('Salário: '))
anos_empresa = int(input('Quantidade de anos de empresa: '))

if anos_empresa <= 3:
     aumento = salario * 0.03
     novo_salario = salario + aumento
     print(f'O novo salário do funcionário {nome} é de: {novo_salario:.2f}')

elif anos_empresa < 10:
     aumento = salario * 0.125
     novo_salario = salario + aumento
     print(f'O novo salário do funcionário {nome} é de: {novo_salario:.2f}')
else:
     aumento = salario * 0.20
     novo_salario = salario + aumento
     print(f'O novo salário do funcionário {nome} é de: {novo_salario:.2f}')