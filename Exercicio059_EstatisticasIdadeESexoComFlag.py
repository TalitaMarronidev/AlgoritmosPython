# 59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
#a) qual é a maior idade lida
#b) quantos homens foram cadastrados
#c) qual é a idade da mulher mais jovem
#d) qual é a média de idade entre os homens

continuar = " "
maiorIdade = 0
homens = 0
soma = 0
primeiraMulher = True

while continuar != "n":
    sexo = input("Sexo:(f/m)").lower()
    idade = int(input("Idade: "))

    if idade > maiorIdade:
        maiorIdade = idade

    if sexo == "m":
        homens += 1
        soma += idade


    if sexo == "f":
        if primeiraMulher:
            mulherMaisJovem = idade
            primeiraMulher = False

        elif idade < mulherMaisJovem:
            mulherMaisJovem = idade

    

    continuar = input("Você quer continuar?? (s/n)").lower()

if homens > 0:
    media = soma / homens
else:
    media = 0

print("DADOS: ")
print(f'A maior idade é de: {maiorIdade}')
print(f'Foram cadastrados {homens} homens')
print(f'A mulher mais jovem tem {mulherMaisJovem} anos')
print(f'A media de idade dos homens é de: {media}')