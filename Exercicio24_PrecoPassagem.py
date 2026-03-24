#24) Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.

km = float(input('Qual a quantidade de km que deseja percorrer: '))
if km <= 200:
    valor = km * 0.50
    print(f'O valor da sua passagem é de: {valor:.2f}')
else:
    valor = km * 0.45
    print(f'O valor da sua passagem é de: {valor:.2f}')
