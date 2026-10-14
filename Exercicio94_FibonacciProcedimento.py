#94) [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos termos da sequência serão mostrados na tela. O seu procedimento
#  deve receber esse valor e mostrar a quantidade de elementos solicitados.
#Obs: Use os exercícios 70 e 75 para te ajudar na solução
#Ex:
#Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
#Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM



def Fibonacci(num):

        a = 1
        b = 1
        print(a, end=" >> ")
        print(b, end=" >> ")

        for _ in range(num - 2):
            c = a + b
            print(c, end=" >> ")
    
            a = b
            b = c

        print("FIM!")
Fibonacci(5)
print()
Fibonacci(9)
