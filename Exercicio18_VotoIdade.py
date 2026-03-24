#18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.

ano_nascimento = int(input('Ano de nascimento: '))
idade = 2025 - ano_nascimento

if idade >= 18:
    print('Você pode votar')
else:
    print('Você é menor de idade, não pode votar')