#96) Crie um programa que tenha uma função Media(), que vai receber as 2 notas de um aluno e retornar a sua média para o programa principal.

def Media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

resultado = Media(8, 5)
print(resultado)