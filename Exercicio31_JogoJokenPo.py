#31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

import random

print('-------------MENU---------------')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')

op = int(input('Informe a opção escolhida: '))


computador = random.randint(1, 3)

if op == 1:
    jogador = 'Pedra'
elif op == 2:
    jogador = 'Papel'
elif op == 3:
    jogador = 'Tesoura'

if computador == 1:
    pc = 'Pedra'
elif computador == 2:
    pc = 'Papel'
elif computador == 3:
    pc = 'Tesoura'

print(f'Você escolheu: {jogador}')
print(f'O computador escolheu: {pc}')

#Verificação se o usuário digitar 1, e as três possibilidades do computador
if (op == 1) and (computador == 1):
    print('Deu empate')
elif (op == 1) and (computador == 2):
    print('Computador ganhou')
elif (op == 1) and (computador == 3):
    print('Você ganhou')

#Verificação se o usuário digitar 2, e as três possibilidades do computador
if (op == 2) and (computador == 1):
    print('Você ganhou')
elif (op == 2) and (computador == 2):
    print('Deu empate')
elif (op == 2) and (computador == 3):
    print('Computador ganhou')

#Verificação se o usuário digitar 3, e as três possibilidades do computador
if (op == 3) and (computador == 1):
    print('Computador ganhou')
elif (op == 3) and (computador == 2):
    print('Você ganhou')
elif (op == 3) and (computador == 3):
    print('Deu empate')