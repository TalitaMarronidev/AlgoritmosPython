#52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
#a) Qual é a média de idade do grupo
#b) Quantas pessoas tem mais de 18 anos
#c) Quantas pessoas tem menos de 5 anos
#d) Qual foi a maior idade lida

contador = 1
soma = 0
maior18 = 0
menor5 = 0

while (contador <= 10):
    idade = int(input("Idade: "))
    soma += idade
    

    if (contador == 1): 
            maior = idade
    
    if (idade > maior):
            maior = idade

    if (idade > 18):
        maior18 += 1

    if(idade < 5):
        menor5 += 1

    contador += 1

   
media = soma / 10
print(f'A media da idade do grupo é de: {media}')
print(f'Tem {maior18} pessoas maiores que 18 anos')
print(f'Tem {menor5} pessoas menores que 5 anos')
print(f'A maior idade é de {maior}')
