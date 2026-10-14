#88) Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem várias vezes
#Ex: Ao chamar Gerador("Aprendendo Python", 4) aparece:
#+-------=======------+
# Aprendendo Python
# Aprendendo Python
# Aprendendo Python
# Aprendendo Python
#+-------=======------+


def gerador(mensagem, quantidade):
    print("+-------=======------+")

    for _ in range(quantidade):
        print(mensagem)
    print("+-------=======------+")
gerador("Aprendendo Python", 4)