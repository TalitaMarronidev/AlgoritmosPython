# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa vai parar quando for digitada a idade 999. No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo.

idade = 0
alunos = 0
soma = 0
media = 0

while idade != 999:
    idade = int(input("Idade do aluno: "))

    if idade != 999:
        alunos += 1
        soma += idade


if alunos > 0:
    media = soma / alunos
else:
    media = 0
    
print("DADOS DA TURMA:")
print(f'Tem {alunos} alunos nessa turma')
print(f'A média de idade dessa turma é de: {media}')