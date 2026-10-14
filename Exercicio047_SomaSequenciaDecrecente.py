#47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0

num = 500
soma = 0
while (num >= 0):
    print(num, end=" ")
    soma += num
    num -= 50

print(f'\nO resultado da expressão acima é de: {soma}') 