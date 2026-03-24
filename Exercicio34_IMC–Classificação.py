#34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
# - abaixo de 18.5: Abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - entre 25 e 30: Sobrepeso
# - entre 30 e 40: Obesidade
# - acima de 40: Obseidade mórbida
#Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado da altura)

print('----------- Índice de Massa Corpórea (IMC)------------')
alt = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso/(alt**2)
print(f'Seu IMC é de : {imc:.2f} kg/m²')

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')