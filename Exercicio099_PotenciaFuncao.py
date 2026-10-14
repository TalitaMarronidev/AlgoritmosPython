#99) Faça um programa que possua uma função chamada Potencia(), que vai receber dois parâmetros numéricos (base e expoente) e vai calcular o resultado da exponenciação.
#Ex: Potencia(5,2) vai calcular 52 = 25 



def Potencia(base, expoente):
    resultado = base ** expoente
    return resultado

resultado = Potencia(5,2)
print(resultado)