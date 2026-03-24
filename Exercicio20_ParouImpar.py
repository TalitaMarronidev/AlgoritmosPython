#20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ouÍMPAR.

print(' ----- PAR OU ÍMPAR-------')
num = int(input('Informe um número:'))

if (num % 2 == 0):
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')