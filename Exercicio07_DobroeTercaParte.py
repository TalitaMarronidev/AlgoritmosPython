#7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte. 
#Ex:  
#Digite um número: 3.5 
#O dobro de 3.5 é 7.0 
#A terça parte de 3.5 é 1.16666

valor = float(input('Digite um número: '))
dobro = valor * 2
tParte = valor / 3

print(f'Dobro de {valor} é: {dobro}')
print(f'A terça parte de {valor} é {tParte}')