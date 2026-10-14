#87) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem personalizada, passada como parâmetro.
#Ex: Ao chamar Gerador("Aprendendo Python") aparece:
#+-------=======------+
# Aprendendo Python
#+-------=======------+



def gerador(mensagem):
    print("+-------=======------+")
    print(mensagem)
    print("+-------=======------+")

gerador("Apredendo Python")