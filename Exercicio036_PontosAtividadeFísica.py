#36) Um programa de vida saudavel quer dar pontos atividades fisicas que podem ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade fisica no mes vale pontos
# - ate 10h de atividade no mes: ganha 2 pontos por hora
# - de 10h ate 20h de atividade no mes: ganha 5 pontos por hora
# - acima de 20h de atividade no mes: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
#Faca um programa que leia quantas horas de atividade uma pessoa teve por mes, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

hrsAtividades = int(input("Informe quantas horas de atividade você teve por mês:"))
pontos = 0
dinheiro = 0

if hrsAtividades <= 10:
    pontos = hrsAtividades * 2
  

elif hrsAtividades <=20:
    pontos = hrsAtividades * 5

else:
    pontos = hrsAtividades * 10

dinheiro = pontos * 0.05

print(f"Pontos: {pontos}");
print (f"Você ganhou {dinheiro:.2f} esse mês")