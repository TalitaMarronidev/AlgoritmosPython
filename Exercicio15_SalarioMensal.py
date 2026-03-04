#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o  salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.

dias = int(input('Informe os dias trabalhados: '))

horas = 8 * dias
valor = horas * 25

print(f'O salário desse funcionário é de: {valor:.2f}')