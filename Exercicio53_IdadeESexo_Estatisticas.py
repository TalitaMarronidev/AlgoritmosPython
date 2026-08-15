#53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
#a) Quantos homens foram cadastrados
#b) Quantas mulheres foram cadastradas
#c) A média de idade do grupo
#d) A média de idade dos homens
#e) Quantas mulheres tem mais de 20 anos

contador = 1
soma = 0
homens = 0
mulheres = 0
somaHomens = 0
mediaHomem = 0 
mulherMaior20 = 0

while (contador <= 5):
    idade = int(input("Idade: "))
    soma += idade
    sexo = input("Sexo: (f/m)").lower()

    if (sexo == "m"):
        homens += 1
        somaHomens += idade

    elif (sexo == "f"):
        mulheres += 1

        if (idade > 20):
            mulherMaior20 += 1

    contador += 1

media = soma / 5

if homens > 0:
    mediaHomem = somaHomens / homens
else:
    mediaHomem = 0

print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastrados {mulheres} mulheres')
print(f'A média do grupo é de {media}')
print(f'A media de idades dos homens é de {mediaHomem}')
print(f'Tem {mulherMaior20} mulheres que tem mais de 20 anos')
    