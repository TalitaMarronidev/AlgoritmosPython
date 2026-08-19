#75) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 15 posições com os primeiros elementos da sequência de Fibonacci:
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

numeros = []
numeros.append(1)
numeros.append(1)




for contador in range(1,14):
    proximo = numeros[-1] + numeros[-2]

    numeros.append(proximo)

print(numeros)