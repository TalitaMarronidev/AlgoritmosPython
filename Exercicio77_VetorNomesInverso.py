#77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados. 

nomes = []

for contador in range (1,8):
    nome = input("Nome: ")
    nomes.append(nome)


nomes.reverse()
print(nomes)

