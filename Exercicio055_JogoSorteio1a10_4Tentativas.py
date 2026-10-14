#55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o
#  computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar
#  acertar.

import random

print('-----ADIVINHE O VALOR SORTEADO PELO COMPUTADOR-----')

computador = random.randint(1, 10)

contador = 1
acertou = False

while (contador <= 4):
    numero = int(input("Informe um número:"))

    if (numero == computador):
        print("Você Acertou!!")
        acertou = True
        break
    else:
        print("Você errou!!")
        
    contador += 1

if not acertou:
    print("Você perdeu!")
    print(f"O número era {computador}")


