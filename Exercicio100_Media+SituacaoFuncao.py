#100) Melhore o exercício 96, criando além da função Media() uma outra função chamada Situacao(), que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber
#  como parâmetro o resultado retornado pela função Media().

def Media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

resultado = Media(8, 5)
print(resultado)

def Situacao(resultado):
    if resultado <= 5:
        return("REPROVADO!")
    elif resultado<7:
        return("RECUPERAÇÃO!")
    else:
        return("APROVADO!")


situacao = Situacao(resultado)
print(situacao)