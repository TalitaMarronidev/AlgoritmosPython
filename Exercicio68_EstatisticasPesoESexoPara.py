#68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
#a) Quantas mulheres foram cadastradas
#b) Quantos homens pesam mais de 100Kg
#c) A média de peso entre as mulheres
#d) O maior peso entre os homens

mulher = 0
soma = 0
homensMais100 = 0
maiorPeso = 0

for pessoas in range (1, 9):
    sexo = input("Sexo (f/m").lower()
    peso = float(input("Peso: "))

    if sexo == "f":
        mulher += 1
        soma += peso

    if sexo == "m":
        if peso > 100:
            homensMais100 += 1

        if peso > maiorPeso:
            maiorPeso = peso

print(f'Foram cadastradas {mulher} mulheres')
print(f'{homensMais100} homens pesam mais de 100kg')

if mulher > 0:
    media = soma / mulher
else:
    media = 0

print(f'A média de peso entre as mulheres é de: {media}')

if maiorPeso == 0:
    print("Nenhum homem foi cadastrado!!")
else:
    print(f'O maior peso entre os homens é de: {maiorPeso}')