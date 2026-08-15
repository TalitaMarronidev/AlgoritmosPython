# 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
#a) Quais foram os números sorteados
#b) Quantos números estão acima de 5
#c) Quantos números são divisíveis por 3

import random

contador = 1
numero = 0
acima5 = 0
div3 = 0


while (contador <= 20):
    numero = random.randint(0, 10)
    print(numero, end=" ")
    contador += 1

    if (numero > 5):
        acima5 += 1
    if (numero % 3 == 0):
        div3 += 1

print(f'\nTem {acima5} números acima de 5')
print(f'Tem {div3} números que são divisíveis por 3')

