#98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
#Ex:
#SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
#SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85



def SuperSomador(inicio, fim):
    soma = 0
    for contador in range(inicio, fim + 1):
        soma += contador

    return soma

soma = SuperSomador(1,6)
print(soma)
soma = SuperSomador(15,19)
print(soma)