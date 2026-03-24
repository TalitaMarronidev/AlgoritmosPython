#25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente, para três segmentos
# formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.

print('--------VERIFICAÇÃO TRIÂNGULO------------')
seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')