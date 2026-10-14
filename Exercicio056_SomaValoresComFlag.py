#56) Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
#Obs: O programa será interrompido quando o número 1111 for digitado

soma = 0
numero = 0

while numero != 1111:
    numero = int(input("Informe um número"))

    if numero != 1111:
        soma += numero
        
print(f'A soma dos números é de: {soma}')