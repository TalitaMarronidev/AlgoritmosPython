#90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Somador() que vai calcular e mostrar a soma entre eles.

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

def Somador(num1, num2):
    soma = num1 + num2
    print(soma)

Somador(num1,num2)