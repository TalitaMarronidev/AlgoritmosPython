#22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

anoNascimento = int(input('Digite o ano de nascimento: '))
idade = 2025 - anoNascimento

if idade < 18:
    tempo = 18 - idade
    print(f'Falta {tempo} anos para o seu alistamento!')
else:
    tempo = idade - 18
    print(f'Já se passaram {tempo} anos para o seu alistamento!')
