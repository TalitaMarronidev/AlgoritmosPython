#45) O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.

valorInicial = int(input("Informe o valor inicial da contagem: "))
valorFinal = int(input("Informe o valor final da contagem: "))
incremento = int(input("Informe o valor do incremento: "))

while incremento <= 0:
    incremento = int(input("Digite um incremento maior que zero: "))

if (valorInicial < valorFinal):
    while(valorInicial <= valorFinal):
        print(valorInicial, end=" ")
        valorInicial += incremento
elif (valorInicial > valorFinal):
    while(valorInicial >= valorFinal):
         print(valorInicial, end=" ")
         valorInicial -= incremento
else:
    print("Não é possível fazer a contagem, pois os dois valores são iguais.")

print("Acabou!!")