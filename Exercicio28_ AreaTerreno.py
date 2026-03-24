#28) Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também deve mostrar a classificação desse terreno, de acordo
# com a lista abaixo:
# - Abaixo de 100m² = TERRENO POPULAR
# - Entre 100m² e 500m² = TERRENO MASTER
# - Acima de 500m² = TERRENO VIP

larg = int(input('Informe a largura do terreno: '))
comp = int(input('Informe a comprimento do terreno: '))

area = larg * comp
print(f'A área é de: {area}')

if area < 100:
    print('Classificação do terreno: POPULAR')
elif area <= 500:
    print('Classificação do terreno: MASTER')
else:
    print('Classificação do terreno: VIP')