#85) Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e guarde esses dados em três vetores. No final, mostre uma listagem contendo apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.

nomes = []
sexoFuncionarios = []
salarios = []

for contador in range(5):
    nome = input('Nome: ')
    sexo = input('Sexo: (f/m)').lower()
    salario = float(input('Salário: '))

    nomes.append(nome)
    sexoFuncionarios.append(sexo)
    salarios.append(salario)
    print()


print('Essas são as mulheres que recebem mais de R$ 5000 reais')
for i in range(5):
    if sexoFuncionarios[i] == 'f' and salarios[i] > 5000:
        print(f'Nome: {nomes[i]}')
        print(f'Sexo: {sexoFuncionarios[i]}')
        print(f'Salário: R$ {salarios[i]:.2f}')
        print()

