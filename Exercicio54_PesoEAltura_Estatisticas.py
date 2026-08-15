#54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
#a) Qual foi a média de altura do grupo
#b) Quantas pessoas pesam mais de 90Kg
#c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
#d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

contador = 1
somaAltura = 0
maior90 = 0
menos50e160 = 0
mais190e100 = 0

while (contador <= 7):
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    somaAltura += altura

    if (peso > 90):
        maior90 += 1

    if (peso < 50 and altura < 1.60):
        menos50e160 += 1

    if (altura > 1.90 and peso > 100):
        mais190e100 += 1

    contador += 1

media = somaAltura / 7

print(f'Média de altura do grupo: {media:.2f}')
print(f'{maior90} pessoas pesam mais de 90kg')
print(f'{menos50e160} pessoas pesam menos de 50kg e tem menos de 1.60m de altura')
print(f'{mais190e100} pessoas medem mais de 1.90m e pesam mais de 100kg')

