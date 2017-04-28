"""Como um exercício, modifique o programa para corrigir este erro."""

prefixos = "JKLMNOPQ"
sufixo = "ack"
for letra in prefixos:
    if letra == "O" or letra == "Q":
        print (letra + "u" + sufixo)
    else:
        print (letra + sufixo)
