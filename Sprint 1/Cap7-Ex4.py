"""Como um exercício, encapsule este código em
uma função chamada contaLetras, e generalize-a de modo
que possa aceitar uma string e uma letra como parâmetros."""

def contaLetras(str, x): #defini a função
    contador = 0 #iniciei o contador
    for letra in str: #enquanto tiver letra na string, executar
        if letra == x: #se letra for igual a letra escolhida
            contador = contador + 1 #soma o contador
    return contador #retorna o contador

string = input("Digite uma palavra: " ) 
letra = input("Digite a Letra: ")
qtidade = contaLetras(string, letra)
print (qtidade)

"""Obs: Para ter um resultado mais concreto, seria necessario
padronizar, por exemplo, ao colocar Ana Paula, com o A e o P
maiusculo, e perguntar quantos a's tem na funcao, retorna 3,
mas sabemos que é 4, pois para o programa A != a)"""
