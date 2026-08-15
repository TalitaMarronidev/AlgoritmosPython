#37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse 
# funcionário trabalha na empresa.No final, mostre o seu novo salário, baseado na tabela a seguir:
#- Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
#- Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario = float(input("Informe o seu salário atual: "))
genero = input("Informe o seu gênero: (f/m)").lower()
anos = int(input("Há quantos anos trabalha na empresa: "))
aumento = 0

if (genero == "f"):
    if (anos < 15):
        aumento = salario + (salario * 0.05)
    elif (anos <= 20):
        aumento = salario + (salario * 0.12)
    else:
         aumento = salario + (salario * 0.23)

elif (genero == "m"):
    if (anos < 20):
            aumento = salario + (salario * 0.03)
    elif (anos <= 30):
            aumento = salario + (salario * 0.13)
    else:
             aumento = salario + (salario * 0.25)
else:
    print("Gênero inválido!")

print(f'Salário atual: {salario:.2f}')
print(f'Salário atualizado: {aumento:.2f}')