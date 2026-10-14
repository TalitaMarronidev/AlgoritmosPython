#83) [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os números gerados e depois coloque o vetor em ordem crescente,
#  mostrando no final os valores ordenados.

import random

numeros = []
numero = 0

for contador in range (1, 21):
    numero = random.randint(0, 99)
    numeros.append(numero)

print(f'Números gerados pelo computador: {numeros}')
numeros.sort()
print(f'Números em ordem crescente{numeros}')