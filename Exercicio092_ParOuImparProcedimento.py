#92) Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

num = int(input("Numero: "))

def ParOuImpar(num):
    if num%2==0:
        print(f'O numero {num} eh par')
    else:
        print(f'O numero {num} eh impar')

ParOuImpar(num)