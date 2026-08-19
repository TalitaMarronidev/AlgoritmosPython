#74) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
#5 3 5 3 5 3 5 3 5 3

numeros = []

for contador in range(10):
    if contador % 2 == 0:
        numeros.append(5)
    else:
        numeros.append(3)

print(numeros, end= " ")