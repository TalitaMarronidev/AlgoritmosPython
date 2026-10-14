#84) Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses valores em dois vetores, em posições relacionadas. No final, mostre uma listagem contendo apenas os dados das pessoas menores de idade.

nomes = []
idades = []
nome = " "
idade = 0
menorDeIdade = []

for contador in range(1,10):
    nome = input("Nome: ")
    nomes.append(nome)
    idade = int(input("Idade: "))
    idades.append(idade)

    if idade < 18:
        menorDeIdade.append(nome)
        menorDeIdade.append(idade)

print(menorDeIdade)