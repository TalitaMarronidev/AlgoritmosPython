#17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada
# Km acima da velocidade permitida.

velocidade = int(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print('Você foi multado!!')
    multa = velocidade - 80
    valor = multa * 5
    print(f'Valor da multa foi R${valor}')
else:
    print('Pode seguir viagem!')