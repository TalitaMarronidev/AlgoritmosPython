#30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes



print('--------VERIFICAÇÃO DO TIPO TRIÂNGULO------------')
seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    if seg1 == seg2 == seg3:
        print('É um triângulo equilátero')
    elif (seg1 == seg2) or (seg2 == seg3) or (seg1 == seg3):
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')
else:
    print('Não é possível formar um triângulo')