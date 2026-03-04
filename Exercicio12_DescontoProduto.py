#12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

preco = float(input('Informe o preço do produto:'))

desconto = preco * 0.05
precoDesconto = preco - desconto

print(f'O produto com desconto é de: {precoDesconto:.2f}')