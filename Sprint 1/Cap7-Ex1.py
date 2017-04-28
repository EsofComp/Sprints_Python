"""Como um exercício, escreva uma função que tome uma string
como argumento e devolva suas letras de
trás para frente, uma por linha."""

def contrario(string):
    indice = len(string)
    indice = indice - 1
    while indice > -1:
        letra = string[indice]
        print (letra)
        indice = indice - 1

string = input('Digite uma palavra: ')
contrario(string)


