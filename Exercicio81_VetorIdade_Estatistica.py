#81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No final, mostre:
#a) Qual é a média de idade das pessoas cadastradas
#b) Em quais posições temos pessoas com mais de 25 anos
#c) Qual foi a maior idade digitada (podem haver repetições)
#d) Em que posições digitamos a maior idade

idades = []
soma = 0
mais25 = []
posicaoMaiorIdade = []

for contador in range(8):
    idade = int(input("Idade: "))
    idades.append(idade)
    soma += idade

    if idade > 25:
        mais25.append(contador)

maiorIdade = max(idades)

for contador in range(len(idades)):
    if idades[contador] == maiorIdade:
        posicaoMaiorIdade.append(contador)

media = soma / len(idades)

print(f'Média: {media}')
print(f'Temos pessoas maiores que 25 anos nas seguintes posições: {mais25}')
print(f'Qual foi a maior idade digitada: {maiorIdade}')
print(f'A maior idade foi digitada nas posições: {posicaoMaiorIdade}')