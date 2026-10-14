#44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
#Ex: Digite o primeiro Valor: 3
#Digite o último Valor: 10
#Digite o incremento: 2
#Contagem: 3 5 7 9 Acabou!

valorInicial = int(input("Informe o valor inicial da contagem: "))
valorFinal = int(input("Informe o valor final da contagem: "))
incremento = int(input("Informe o valor do incremento: "))

while incremento <= 0:
    incremento = int(input("Digite um incremento maior que zero: "))

while(valorInicial <= valorFinal):
    print(valorInicial, end=" ")
    valorInicial += incremento

print("Acabou!!")