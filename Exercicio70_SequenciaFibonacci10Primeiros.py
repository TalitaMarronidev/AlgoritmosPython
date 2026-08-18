#70) [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci:
#1 1 2 3 5 8 13 21...

a = 1
b = 1
c= a + b
print(a,b,end=" ")

for contador in range(1,9):
    c = a + b

    print(c, end=" ")

    a = b
    b = c 
    