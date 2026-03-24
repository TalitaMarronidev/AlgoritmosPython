#33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos_pagamento = int(input('Informe a quantidade de anos que irá pagar: '))

prestacao = valor_casa / (anos_pagamento * 12)

porcentagem = salario * 0.30

print(f'Valor da prestação: {prestacao:.2f}')
print(f'Valor aprovado para o comprador: {porcentagem:.2f}')

if prestacao <= porcentagem:
    print('O empréstimo foi aprovado!')
else:
    print('O empréstimo foi negado!')