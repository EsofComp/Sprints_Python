"""Como um exercício, modifique a função find (encontrar) de modo que ela
receba um terceiro parâmetro, o índice da string por onde ela deve começar
sua procura."""

def find(str, ch, first):
    indice = first
    while indice < len(str):
        if str[indice] == ch:
            return indice + 1
        indice = indice + 1
    return -1

string = input("Digite uma String: ")
escolhida = input("Digite a letra que quer saber a posição: ")
dica = int(input("Digite a partir de onde começar a procurar: "))
result = find(string, escolhida, dica)
print (result)

