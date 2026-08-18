#69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e a soma entre 
# todos os valores da sequência.

primeiroTermo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

termo = primeiroTermo
soma = 0

for contador in range(1,11):
    print(termo)
    soma += termo
    termo += razao
    

print(f'A soma de todos os números é de: {soma}')