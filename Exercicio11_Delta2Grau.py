#11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

a = int(input('Informe o valor de a:'))
b = int(input('Informe o valor de b:'))
c = int(input('Informe o valor de c:'))

delta = (b**2) - (4*a*c)
print(f'O resultado de delta é de: {delta:.2f}')