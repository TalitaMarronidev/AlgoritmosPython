#26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:
# - O primeiro valor é o maior
# - O segundo valor é o maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Não existem valor maior, os dois são iguais!')