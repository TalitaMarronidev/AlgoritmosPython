#51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

contador = 1

while (contador <= 8):
    preco = float(input("Informe o preço do produto: "))

    if (contador == 1):
        maior = preco
        menor = preco

    if (preco > maior):
        maior = preco

    if (preco < menor):
        menor = preco

    contador += 1

print(f'O menor valor é de: {menor}')
print(f'O maior valor é de: {maior}')