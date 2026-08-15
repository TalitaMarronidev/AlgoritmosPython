# 62) Faça um programa que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o 
# usuário decidir parar, mostre na tela:
#a) Quantas idades foram digitadas
#b) Qual é a média entre as idades digitadas
#c) Quantas pessoas tem 21 anos ou mais.


continuar = ""
idades = 0
soma = 0
PessoasMaisIgual21 = 0


while continuar != "n":
    idade = int(input("Idade: "))
    idades += 1
    soma += idade

    if idade >= 21:
        PessoasMaisIgual21 += 1


    continuar = input("Voce quer continuar? (s/n)").lower()

print("Dados: ")
print((f'Foram digitadas {idades}'))

if idades > 0:
    media = soma / idades
else:
    media = 0

print(f'A média entre as idades difigitadas é de: {media}')
print(f'Tem {PessoasMaisIgual21} que tem 21 anos ou mais')
