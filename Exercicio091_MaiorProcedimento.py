#91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma 
# mensagem informando essa característica.


num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

def Maior(num1, num2):
    if num1 > num2:
        print(f'O maior número é: {num1}')
    elif num2 > num1:
        print(f'O maior número é: {num2}')
    else:
        print("Os números são iguais.")

Maior(num1, num2)