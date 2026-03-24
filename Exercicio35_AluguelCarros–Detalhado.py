# 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por
# Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

print('------ Aluguel de Carros ------')

tipo_carro = int(input('Informe o tipo do carro alugado (1 - Popular / 2 - Luxo): '))
dias = int(input('Informe a quantidade de dias em que alugou o carro: '))
km = float(input('Informe a quantidade de km percorrido: '))

# Inicializa variáveis
valor_dia = 0
valor_km = 0

# Define o valor por dia e o preço por km
if tipo_carro == 1:  # Popular
    valor_dia = 90
    if km <= 100:
        valor_km = 0.20

    else:
        valor_km = 0.10


elif tipo_carro == 2:  # Luxo
    valor_dia = 150
    if km <= 200:
        valor_km = 0.30
    else:
        valor_km = 0.25
else:
    print('Tipo de carro inválido!')

# Se o tipo de carro for válido, calcula o total
if valor_dia > 0:
    valor_dias = dias * valor_dia
    valor_km_total = km * valor_km
    valor_total = valor_dias + valor_km_total

    print(f'Valor pelos dias: R${valor_dias:.2f}')
    print(f'Valor pelos km: R${valor_km_total:.2f}')
    print(f'Valor total a ser pago: R${valor_total:.2f}')