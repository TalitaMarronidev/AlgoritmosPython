#60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
#a) O nome da pessoa mais velha
#b) O nome da mulher mais jovem
#c) A média de idade do grupo
#d) Quantos homens tem mais de 30 anos
#e) Quantas mulheres tem menos de 18 anos

continuar = ""
maisvelho = 0
primeiraMulher = True
soma = 0
pessoas = 0
HomemMais30 = 0
MulherMenos18 = 0

while continuar != "n":
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (f/m)").lower()

    if idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome

    if sexo == "f":
        if primeiraMulher:
            mulherMaisJovem = idade
            nomeMulherMaisJovem = nome
            primeiraMulher = False  
        elif idade < mulherMaisJovem:
            mulherMaisJovem = idade
            nomeMulherMaisJovem = nome

        if idade < 18:
            MulherMenos18 += 1

    soma += idade
    pessoas += 1


    if sexo == "m":
        if idade > 30:
            HomemMais30 += 1

    continuar = input("Você quer continuar? (s/n)").lower()

media = soma / pessoas

print('DADOS:')
print(f'Nome da pessoa mais velha: {nomemaisvelho}')

if primeiraMulher:
    print("Nenhuma mulher foi cadastrada")
else:
    print(f'Nome da mulher mais jovem: {nomeMulherMaisJovem}')

print(f'Nome da mulher mais jovem: {nomeMulherMaisJovem}')
print(f'Média de idade do grupo: {media}')
print(f'Tem {HomemMais30} homens que tem mais de 30 anos')
print(f'Tem {MulherMenos18} mulheres que tem menos de 18 anos')
