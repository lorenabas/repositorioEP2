def cria_baralho():
    baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    return baralho

def extrai_naipe(carta):
    if carta[1] == '♦' or carta[1] == '♥' or carta[1] == '♣' or carta[1] == '♠':
        return carta[1]
    elif carta[2] == '♦' or carta[2] == '♥' or carta[2] == '♣' or carta[2] == '♠':
        return carta[2]

def extrai_valor(carta):
    if carta[1] == '0':
        return '10'
    else:
        return carta[0]

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

def possui_movimentos_possiveis(l_baralho):
    v_ou_f = False
    for i in range(len(l_baralho)):
        if lista_movimentos_possiveis(l_baralho, i) != []:
            v_ou_f = True
    
    return v_ou_f
    
def empilha(l_baralho, p_inicial, p_final):
    valor_inicial = l_baralho[p_inicial]
    valor_no_destino = l_baralho[p_final]

    l_baralho[p_final] = valor_inicial
    l_baralho.pop(p_inicial)

    return l_baralho

