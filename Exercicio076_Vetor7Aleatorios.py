#76) Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela.

import random

numeros = []

for contador in range(1,8):
    numeros.append(random.randint(0,10))

print(numeros)