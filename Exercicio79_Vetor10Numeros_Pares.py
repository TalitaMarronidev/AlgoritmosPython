#79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.No final, mostre quais são os números pares que foram digitados e em que posições eles estão armazenados.

numeros = []
pares = []
posicoes = []

for contador in range (10):
        numero = int(input("Número: "))
        numeros.append(numero)

        if numero % 2 == 0:
            pares.append(numero)
            posicoes.append(contador)
         
          

print(f'Os números pares que foram digitador: {pares}')
print(f'A posição dos números pares: {posicoes}')