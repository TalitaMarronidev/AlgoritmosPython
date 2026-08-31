#78) Escreva um programa que leia 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram digitados valores que são múltiplos de 10.

numeros = []
multiplos10 = []

for contador in range (1,16):
    numero = int(input("Número: "))
    numeros.append(numero)


    if numero % 10 == 0:
        multiplos10.append(contador - 1)


print(numeros)
print(multiplos10)
