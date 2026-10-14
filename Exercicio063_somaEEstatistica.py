#63) Crie um programa que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
#a) O somatório entre todos os valores
#b) Qual foi o menor valor digitado
#c) A média entre todos os valores
#d) Quantos valores são pares

continuar = ""
soma = 0
numeros = 0
pares = 0
primeiroNumero = True
valoresPares = 0


while continuar != "n":
    numero = int(input("Número: "))
    numeros += 1
    soma += numero

    if primeiroNumero:
        menorValor = numero
        primeiroNumero = False
    elif numero < menorValor:
        menorValor = numero

    if numero % 2 == 0:
        valoresPares += 1
        


    continuar = input("Voce quer continuar? (s/n) ").lower()

if numeros > 0:
    media = soma / numeros
else:
    media = 0

     
print(f'A soma de todos os valores é de: {soma}')
print(f'O menor valor digitado é de: {menorValor}')
print(f'A média dos valores é de: {media}')
print(f'{valoresPares} números são pares')
