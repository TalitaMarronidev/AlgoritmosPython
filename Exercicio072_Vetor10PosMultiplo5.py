# 72) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
#5 10 15 20 25 30 35 40 45 50

numeros5 = []

for contador in range(1,11):
    numeros5.append(contador * 5)

print(numeros5)