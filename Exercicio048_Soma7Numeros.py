#48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.

contador = 1
soma = 0

while (contador < 7):
    numero = int(input("Informe um número: "))
    soma += numero
    contador += 1

print(f'A soma dos números é de: {soma}')
