#10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura = float(input('Largura da parede: '))
alt = float(input('Altura da parede:'))

area = largura * alt
print(f'A área a ser pintada é de: {area:.2f}')

tinta = area / 2

print(f'São necessários {tinta:.2f} litros de tinta')