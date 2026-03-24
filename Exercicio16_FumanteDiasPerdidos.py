#16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min
# de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.



cigarros_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Há quantos anos você fuma? '))

dias_fumando = anos_fumando * 365
total_cigarros = cigarros_dia * dias_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440
print(f'Você perdeu {dias_perdidos} dias!')