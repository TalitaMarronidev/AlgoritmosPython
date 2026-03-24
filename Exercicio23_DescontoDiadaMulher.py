# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule
# o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input('Qual o seu nome?')
sexo = input('Qual o seu sexo?(M/F)')
valor = float(input('Qual o valor das suas compras?'))

if sexo == 'F':
    desconto = valor * 0.13
    valor_total = valor - desconto
    print(f'Olá {nome}')
    print(f'Valor da compra: {valor}')
    print(f'Valor do desconto: {desconto}')
    print(f'Valor final: {valor_total}')
else:
    desconto = valor * 0.05
    valor_total = valor - desconto
    print(f'Olá {nome}')
    print(f'Valor da compra: {valor}')
    print(f'Valor do desconto: {desconto}')
    print(f'Valor final: {valor_total}')