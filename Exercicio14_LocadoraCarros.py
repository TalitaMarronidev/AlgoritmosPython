#14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

km = int(input('Informe a quantidade de Km percorridos:'))
dias = int(input('Informe a quantidade de dias em que o carro ficou alugado: '))

precoDias = dias * 90
precoKm = km * 0.20
total = precoDias + precoKm

print(' ------------------ VALORES ---------------------')
print(f'Dias: R${precoDias:.2f}')
print(f'KM: R${precoKm:.2f}')
print(f'Valor total: R${total:.2f}')