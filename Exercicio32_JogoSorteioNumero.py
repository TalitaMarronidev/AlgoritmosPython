#32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.

import random

print('-----ADIVINHE O VALOR SORTEADO PELO COMPUTADOR-----')

num = int(input('Informe um numero inteiro de 1 a 5: '))

computador = random.randint(1, 5)


if num == computador:
    print('Você adivinhou!!')
else:
    print('Não foi dessa vez.')
    print(f'Você escolheu {num}')
    print(f'O computador sorteou: {computador}')
