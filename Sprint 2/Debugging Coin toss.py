import random #bilbioteca que torna aleatorio   
escolha = '' #iniciei uma variavel
sorteado = '' # iniciei outra variavel
while escolha not in ('cara', 'coroa'): #faz rodar ate o usuario colocar uma opção valida
    print('Escolha Cara ou Coroa meu bom: ') #Permite a escolha
    escolha = input() #guarda a escollha
    escolha = escolha.lower() #padroniza a escolha
    
sorteio = random.randint(0, 1) # 0 é coroa, 1 é cara.
if sorteio == 0: #condicao, para tranformar um int em string
    sorteado = 'coroa'
elif sorteio == 1:
    sorteado = 'cara'
    
if sorteado == escolha:
    print('Nice, você ganhou!!') #vitoria no jogo
else:
    print('Sorry, vc perdeu!! Tente novamente') #derrota no jogo
    escolha = '' 
    while escolha not in ('cara' , 'coroa'): #nova chance
        print ('Nova escolha:')
        escolha = input()
        escolha = escolha.lower()
        if (escolha == 'cara' or escolha == 'coroa'):
            if sorteio == escolha:
                print('Nice, você ganhou!!')
                break
            else:
                print('Desisti, vc é muito Ruim!!')
                break
        else:
            print("Por favor, escolha entre as opções fornecidas")



    
    
    
