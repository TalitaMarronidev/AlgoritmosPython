#9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
#e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,23.

carteira = float(input('Informe qual o valor que você possui em sua carteira (em R$): '))

dolares = carteira / 5.23
print(f'Você pode comprar {dolares:.2f} dólares!')


