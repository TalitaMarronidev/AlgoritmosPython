#80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e 15 sorteados pelo computador. Depois disso, peça para o usuário digitar um número (chave) e seu programa deve mostrar em que posições essa chave foi
# encontrada. Mostre também quantas vezes a chave foi sorteada.

import random

numeros = []
posicoes = []

# Preenche o vetor com 30 números aleatórios
for contador in range(30):
    numero = random.randint(1, 15)
    numeros.append(numero)

print(numeros)

# Usuário escolhe a chave
chave = int(input("Informe um número: "))

# Procura a chave no vetor
for contador in range(30):
    if numeros[contador] == chave:
        posicoes.append(contador)

print(f'Esse número foi encontrado nas seguintes posições: {posicoes}')
print(f'Esse número foi sorteado {len(posicoes)} vez(es)')