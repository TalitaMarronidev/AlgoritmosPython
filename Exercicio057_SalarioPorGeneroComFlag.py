# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele 
# quer continuar ou não sempre que ler os dados de um funcionário.

continuar = " "
salarioFeminino = 0
salarioMasculino = 0

while continuar != "n":
    salario = float(input("Salário do funcionário:"))
    sexo = input("Sexo do funcionário:(f/m)").lower()

    if (sexo == "m"):
        salarioMasculino += salario

    else:
        salarioFeminino += salario

    continuar = input("Voce quer continuar (s/n)").lower()



print("TOTAL DO SALÁRIO DOS FUNCIONÁRIOS")
print(f'FEMININO: {salarioFeminino}')
print(f'MASCULINO: {salarioMasculino}')
