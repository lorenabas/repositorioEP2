import random
#preto = '\033[30m'
#vermelho = '\033[31m'
#branco = '\033[37m'

#cria baralho e embaralha
def cria_baralho():
    l_baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    l_embaralhada = random.sample(l_baralho, len(l_baralho))
    return l_embaralhada

#situação atual
def sit_atual(l_baralho):
    for carta in l_baralho:
        if extrai_naipe(carta)== '♠' or extrai_naipe(carta) == '♣':
            print("\033[37m{0}. \033[30m{1}".format(l_baralho.index(carta) + 1, carta))
        elif extrai_naipe(carta) == '♥' or extrai_naipe(carta) == '♦':
             print("\033[37m{0}. \033[31m{1}".format(l_baralho.index(carta) + 1, carta))

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

#Jogo:
j = 1
while j != 0:
    print("\033[37m\n Paciência Acordeão")
    print("\033[37m====================\n")
    baralho = cria_baralho()
    while len(baralho) > 2:
        print("\033[37m Situação Atual:")
        print("\033[37m----------------\n")
        sit_atual(baralho)
        print("")
        if possui_movimentos_possiveis(baralho):
            carta_mover = int(input("\033[37mDigite a posição da carta que quer mover (1 - {}):".format(len(baralho))))-1
            print("")
            if carta_movimentos_possiveis(baralho, carta_mover):
                if extrai_naipe(baralho[carta_mover]) == '♠️' or extrai_naipe(baralho[carta_mover]) == '♣':
                    print("\033[37mSobre qual carta você quer empilhar o \033[30m{}\033[37m?".format(baralho[carta_mover]))
                    print("")
                elif extrai_naipe(baralho[carta_mover]) == '♥' or extrai_naipe(baralho[carta_mover]) == '♦':
                    print("\033[37mSobre qual carta você quer empilhar o \033[31m{}\033[37m?".format(baralho[carta_mover]))
                    print("")
                a = True
                while a:
                    if lista_movimentos_possiveis(baralho, carta_mover) == [1]:
                        if extrai_naipe(baralho[(carta_mover-1)]) == '♥' or extrai_naipe(baralho[(carta_mover-1)]) == '♦':
                            print("\033[37m{0}. \033[31m{1}\n".format(1, baralho[carta_mover-1]))
                        elif extrai_naipe(baralho[(carta_mover-1)]) == '♠️' or extrai_naipe(baralho[(carta_mover-1)]) == '♣':
                            print("\033[37m{0}. \033[30m{1}\n".format(1, baralho[carta_mover-1]))
                        carta_a_empilhar = int(input("\033[37mDigite o número da sua escolha (1):"))
                        print("")
                        
                    elif lista_movimentos_possiveis(baralho, carta_mover) == [3]:
                        if extrai_naipe(baralho[(carta_mover-3)]) == '♥' or extrai_naipe(baralho[(carta_mover-3)]) == '♦':
                            print("\033[37m{0}. \033[31m{1}\n".format(1, baralho[carta_mover-3]))
                        elif extrai_naipe(baralho[(carta_mover-1)]) == '♠️' or extrai_naipe(baralho[(carta_mover-1)]) == '♣':
                            print("\033[37m{0}. \033[30m{1}\n".format(1, baralho[carta_mover-3]))
                        carta_a_empilhar = int(input("\033[37mDigite o número da sua escolha (1):"))+1
                        print("")
                        
                    elif lista_movimentos_possiveis(baralho, carta_mover) == [1,3]:
                        if extrai_naipe(baralho[(carta_mover-1)]) == '♥' or extrai_naipe(baralho[(carta_mover-1)]) == '♦':
                            print("\033[37m{0}. \033[31m{1}".format(1, baralho[carta_mover-1]))
                        elif extrai_naipe(baralho[(carta_mover-1)]) == '♠️' or extrai_naipe(baralho[(carta_mover-1)]) == '♣':
                            print("\033[37m{0}. \033[30m{1}".format(1, baralho[carta_mover-1]))
                        if extrai_naipe(baralho[(carta_mover-3)]) == '♥' or extrai_naipe(baralho[(carta_mover-3)]) == '♦':
                            print("\033[37m{0}. \033[31m{1}\n".format(2, baralho[carta_mover-3]))
                        elif extrai_naipe(baralho[(carta_mover-1)]) == '♠️' or extrai_naipe(baralho[(carta_mover-1)]) == '♣':
                            print("\033[37m{0}. \033[30m{1}\n".format(2, baralho[carta_mover-3]))
                        carta_a_empilhar = int(input("\033[37mDigite o número da sua escolha (1 - 2):"))
                        
                    if carta_a_empilhar == 1 and (extrai_naipe(baralho[carta_mover]) == extrai_naipe(baralho[(carta_mover-1)]) or extrai_valor(baralho[carta_mover]) == extrai_valor(baralho[(carta_mover-1)])):
                        empilha(baralho, carta_mover, (carta_mover-1))
                        a = False
                        print("")
                    elif carta_a_empilhar == 2 and (extrai_naipe(baralho[carta_mover]) == extrai_naipe(baralho[(carta_mover-3)]) or extrai_valor(baralho[carta_mover]) == extrai_valor(baralho[(carta_mover-3)])):
                        empilha(baralho, carta_mover, (carta_mover-3))
                        a = False
                        print("")        
                    else:
                        print("\033[37mVocê não selecionou uma opção válida de carta a empilhar.\n")
                        continue
                    
            else:
                print("\033[37mEssa carta não possui movimentos disponíveis. Selecione outra carta.\n")
                continue

        else:
            print("\033[37mNão há mais movimentos possíveis. Você perdeu :(\n")
            jogar_outra_vez = input("\033[37m Você quer jogar outra vez (s/n)?")
            if jogar_outra_vez == "n":
                j-=1
            else:
                continue

    print("\033[37m Você Ganhou!!!!!\n")
    jogar_outra_vez = input("\033[37m Você quer jogar outra vez (s/n)?")
    if jogar_outra_vez == "n":
        j -= 1
    else:
        continue
print("\n\033[37mFim!")