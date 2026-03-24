#27) Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Média: {media}')

if media <= 4.9:
    print('Reprovado')
elif media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')