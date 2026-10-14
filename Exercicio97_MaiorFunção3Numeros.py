#97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma adaptação que vai receber 
# TRÊS números como parâmetro e vai retornar qual foi o maior entre eles.

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

def Maior(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        print("Os números são iguais.")
        return num1
    else:
        if num1 >= num2 and num1 >= num3:
            return num1

        elif num2 >= num1 and num2 >= num3:
            return num2
    
        elif num3 >= num1 and num3 >= num2:
            return num3
        

    
resultado = Maior(num1, num2, num3)
print(resultado)