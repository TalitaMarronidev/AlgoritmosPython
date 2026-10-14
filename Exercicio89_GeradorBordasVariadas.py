#89) Crie um programa que melhore o procedimento Gerador() da questão anterior para que o programador possa escolher uma entre três bordas:
# +-------=======------+ Borda 1
# ~~~~~~~~:::::::~~~~~~~ Borda 2
# <<<<<<<<------->>>>>>> Borda 3
#Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
#~~~~~~~~:::::::~~~~~~~
# Portugol Studio
# Portugol Studio
# Portugol Studio
#~~~~~~~~:::::::~~~~~~~



def gerador(mensagem, quantidade, borda):
    if borda == 1:
        borda_escolhida = "+-------=======------+"

   
    elif borda == 2:
           borda_escolhida = "~~~~~~~~:::::::~~~~~~~"

    elif borda == 3:
           borda_escolhida = "<<<<<<<<------->>>>>>>"

    print(borda_escolhida)
    for _ in range(quantidade):
       
        print(mensagem)
        
    print(borda_escolhida)


gerador("Portugol Studio", 3, 1)
gerador("Portugol Studio", 3, 2)
gerador("Portugol Studio", 3, 3)