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
        if indice < 3:
            anterior_naipe = extrai_naipe(lista_baralho[indice-1])
            anterior_valor = extrai_valor(lista_baralho[indice-1])
            if carta_naipe == anterior_naipe or carta_valor == anterior_valor:
                movimentos_possiveis.append(1)
        
        else:
            anterior_naipe = extrai_naipe(lista_baralho[indice-1])
            anterior_valor = extrai_valor(lista_baralho[indice-1])
            terceriro_anterior_naipe = extrai_naipe(lista_baralho[indice-3])
            terceriro_anterior_valor = extrai_valor(lista_baralho[indice-3])
            if carta_naipe == anterior_naipe or carta_valor == anterior_valor:
                movimentos_possiveis.append(1)
            if carta_naipe == terceriro_anterior_naipe or carta_valor == terceriro_anterior_valor:
                movimentos_possiveis.append(3)

    return movimentos_possiveis