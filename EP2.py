import random
print("Paciência Acordeão")
print("===================")

baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']

#embaralha baralho --> posições que vão ser mostradas
def baralho_mostra(l_baralho):
    random.shuffle(l_baralho)
    return l_baralho

#situação atual
def sit_atual(l_baralho):
    lista_index = []
    for i in range(0,len(l_baralho)):
        lista_index.append(i+1)
        print("{0}. {1}".format(lista_index[i],l_baralho[i]))

# extração do naipe da carta
def extrai_naipe(carta):
    if carta[1] == '♦' or carta[1] == '♥' or carta[1] == '♣' or carta[1] == '♠':
        return carta[1]
    elif carta[2] == '♦' or carta[2] == '♥' or carta[2] == '♣' or carta[2] == '♠':
        return carta[2]

# extração do valor da carta
def extrai_valor(carta):
    if carta[1] == '0':
        return '10'
    else:
        return carta[0]

#movimentos possíveis da carta selecionada
def lista_movimentos_possiveis(lista_baralho, indice):
    movimentos_possiveis = []
    if indice != 0:
        carta_naipe = extrai_naipe(lista_baralho[indice])
        carta_valor = extrai_valor(lista_baralho[indice])
        anterior_naipe = extrai_naipe(lista_baralho[indice-1])
        anterior_valor = extrai_valor(lista_baralho[indice-1])
        if indice < 3:
            if carta_naipe == anterior_naipe or carta_valor == anterior_valor:
                movimentos_possiveis.append(1)
        
        else:
            terceiro_anterior_naipe = extrai_naipe(lista_baralho[indice-3])
            terceiro_anterior_valor = extrai_valor(lista_baralho[indice-3])
            if carta_naipe == anterior_naipe or carta_valor == anterior_valor:
                movimentos_possiveis.append(1)
            if carta_naipe == terceiro_anterior_naipe or carta_valor == terceiro_anterior_valor:
                movimentos_possiveis.append(3)

    return movimentos_possiveis

# o baralho possuí movimentos possíveis?
def possui_movimentos_possiveis(l_baralho):
    v_ou_f = False
    for i in range(len(l_baralho)):
        if lista_movimentos_possiveis(l_baralho, i) != []:
            v_ou_f = True
    
    return v_ou_f

# a carta selecionada possuí movimentos possíveis?
def carta_movimentos_possiveis(l_baralho, indice):
    if lista_movimentos_possiveis(l_baralho, indice) == []:
        return False
    else:
        return True

# empilhamento da carta para a posição desejada:
def empilha(l_baralho, p_inicial, p_final):
    valor_inicial = l_baralho[p_inicial]
    valor_no_destino = l_baralho[p_final]

    l_baralho[p_final] = valor_inicial
    l_baralho.pop(p_inicial)

    return l_baralho


#chama função de embaralhar baralho:
baralho_mostra(baralho)

j = 1
while j != 0:
    print("Situação Atual:")
    print("-----------------")
    sit_atual(baralho)
    while len(baralho) > 2:
        if possui_movimentos_possiveis(baralho):
            carta_mover = int(input("Digite a posição da carta que quer mover (1 - {}): ".format(len(baralho))))
            print("")
            if carta_movimentos_possiveis(baralho, (carta_mover-1)):
                print("Sobre qual carta voce quer empilhar o {}? ".format(baralho[(carta_mover-1)]))
                print("")
                if lista_movimentos_possiveis(baralho, (carta_mover-1)) == [1]:
                    print("{0}. {1}".format(1, baralho[carta_mover-2]))
                    carta_a_empilhar = int(input("Digite o número da sua escolha (1)? "))
                elif lista_movimentos_possiveis(baralho, (carta_mover-1)) == [3]:
                    print("{0}. {1}".format(1, baralho[carta_mover-4]))
                    carta_a_empilhar = int(input("Digite o número da sua escolha (1)? "))
                elif lista_movimentos_possiveis(baralho, (carta_mover-1)) == [1,3]:
                    print("{0}. {1}".format(1, baralho[carta_mover-2]))
                    print("{0}. {1}".format(2, baralho[carta_mover-4]))
                    carta_a_empilhar = int(input("Digite o número da sua escolha (1 - 2)? "))
            else:
                print("Essa carta não possui movimentos disponíveis. Selecione outra carta.")
                print("")
                continue

            jogar_outra_vez = input("Você quer jogar outra vez (s/n)? ")
            if jogar_outra_vez == "n":
                j-=1
            else:
                continue
        else:
            print("Não há mais movimentos possíveis. Você perdeu :(")
            jogar_outra_vez = input("Você quer jogar outra vez (s/n)? ")
            if jogar_outra_vez == "n":
                j-=1
            else:
                continue
