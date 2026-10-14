# 73) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 9 8 7 6 5 4 3 2 1 0

numeros = []

for contador in range (9,-1, -1):
    numeros.append(contador)

print(numeros)

    