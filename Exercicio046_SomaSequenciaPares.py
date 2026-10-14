#46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.

num = 6
soma = 0

while (num <= 100):
    print(num, end=" ")
    soma += num
    num += 2

print(f'\nSoma entre os números: {soma}')