#5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina. 
#Ex:  
#Nota 1: 4.5 
#Nota 2: 8.5 
#A média entre 4.5 e 8.5 é igual a 6.5

nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))

media = (nota1 + nota2) / 2

print(f'A média das notas é de: {media:.2f}')