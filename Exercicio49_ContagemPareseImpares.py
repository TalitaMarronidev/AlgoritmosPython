#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.

contador = 1
par = 0
impar = 0

while (contador <= 6):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    contador += 1

print(f'Tem {par} números pares')
print(f'Tem {impar} números ímpares')