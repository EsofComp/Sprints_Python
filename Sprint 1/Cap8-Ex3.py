"""Como um execício, descreva o relacionamento
entre string.join(string.split(poesia)) e poesia. Eles são o
mesmo para qualquer string? Quando eles seriam diferentes?

O relacionamento entre eles pode ser descrito pelo programa abaixo:"""

import string
poesia = "Minha Terra tem Palmeiras, onde canta o sabia..."
poe = ['oi' , 'tudo' , 'bem']
poesia_1 = poesia.split()
print (poesia_1)
poesia = ' '.join(poesia.split())
print (poesia)

"""
R: Sim, pois como mostra o programa acima, fizemos isso, adicionamos uma string
(que pode ser escolhida previamente ou pelo usuario) e realizamos as funções
pedidas, e o seu resultado é True.
Eles seriam diferentes, somente em casos em que nao transformassemos os int
para strings, o que falharia, ja que Split e Join sao funções da biblioteca
string."""



