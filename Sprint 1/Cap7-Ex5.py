"""Como um segundo exercício, reescreva esta
função de modo que em vez de percorrer a string, ela use a
versão com três parâmetros de find (encontrar) da seção
anterior."""

def contaLetras(str, x, first): #defini a função
    contador = 0 #iniciei o contador
    indice = first #iniciei o indice com a Dica dada pelo usuario
    while indice < len(str): #enquanto indice for menor que tamanho max
        if str[indice] == x: #se a letra for a escolhida
            contador = contador + 1 #aumentamos o contador
        indice = indice + 1 #aumentamos o indice para continuar o laço
    return contador #retorna o contador

string = input("Digite uma palavra: " ) 
letra = input("Digite a Letra: ")
dica = int(input("Digite a partir de onde começar a procurar: "))
qtidade = contaLetras(string, letra, dica)
print (qtidade) #exibe a quantidade de letras

"""Obs: Para ter um resultado mais concreto, seria necessario
padronizar, por exemplo, ao colocar Ana Paula, com o A e o P
maiusculo, e perguntar quantos a's tem na funcao, retorna 3,
mas sabemos que é 4, pois para o programa A != a)"""

