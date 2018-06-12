from time import sleep

jogar = True

jogador_1 = input("Jogador 1, digite seu nome: ").upper()
jogador_2 = input("Jogador 2, digite seu nome: ").upper()
print("Olá {} & {}. Bem vindos ao Jogo da Velha.".format(jogador_1, jogador_2))
sleep(1)
print("{}, você será o Jogador 1".format(jogador_1))
sleep(1)
print("{}, você será o Jogador 2".format(jogador_2))
sleep(1)

vitorias_1 = 0
vitorias_2 = 0

while jogar:

    placar = "{}  {} x {}  {}.".format(jogador_1, vitorias_1, vitorias_2, jogador_2)

    rodada = 1
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_1 = ["X", "O"]

    def vencedor_1():
        print(tabuleiro)
        sleep(1)
        print("Jogador 1 ganhou!!!!!!!!")
        jogo = False
        return jogo

    def vencedor_2():
        print(tabuleiro)
        sleep(1)
        print("Jogador 2 ganhou!!!!!!!!")
        jogo = False
        return jogo

    def empate():
        print(tabuleiro)
        sleep(1)
        print("Empate! Fim de jogo.")
        jogo = False
        return jogo



    tabuleiro_inicial = '''
         |     |     
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     
        '''

    jogo = True

    while jogo:

        jogador = 1

        while jogador <= 2:

            tabuleiro = '''
                 |     |     
              {}  |  {}  |  {}  
            _____|_____|_____
                 |     |     
              {}  |  {}  |  {} 
            _____|_____|_____
                 |     |     
              {}  |  {}  |  {} 
                 |     |     
                '''.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8])

            # verifica se o jogador 1 ganhou:

            if (lista[0] == lista[1] == lista[2]) and lista[0] == "X" or \
               (lista[3] == lista[4] == lista[5]) and lista[3] == "X" or \
               (lista[6] == lista[7] == lista[8]) and lista[6] == "X":
                jogo = vencedor_1()
                vitorias_1 += 1
                break
            elif (lista[0] == lista[3] == lista[6]) and lista[0] == "X" or \
                 (lista[1] == lista[4] == lista[7]) and lista[1] == "X" or \
                 (lista[2] == lista[5] == lista[8]) and lista[2] == "X":
                jogo = vencedor_1()
                vitorias_1 += 1
                break
            elif (lista[0] == lista[4] == lista[8]) and lista[0] == "X" or \
                 (lista[2] == lista[4] == lista[6]) and lista[2] == "X":
                jogo = vencedor_1()
                vitorias_1 += 1
                break

            # verifica se o jogador 2 ganhou:

            elif (lista[0] == lista[1] == lista[2]) and lista[0] == "O" or \
                 (lista[3] == lista[4] == lista[5]) and lista[3] == "O" or \
                 (lista[6] == lista[7] == lista[8]) and lista[6] == "O":
                jogo = vencedor_2()
                vitorias_2 += 1
                break
            elif (lista[0] == lista[3] == lista[6]) and lista[0] == "O" or \
                 (lista[1] == lista[4] == lista[7]) and lista[1] == "O" or \
                 (lista[2] == lista[5] == lista[8]) and lista[2] == "O":
                jogo = vencedor_2()
                vitorias_2 += 1
                break
            elif (lista[0] == lista[4] == lista[8]) and lista[0] == "O" or \
                 (lista[2] == lista[4] == lista[6]) and lista[2] == "O":
                jogo = vencedor_2()
                vitorias_2 += 1
                break
            if rodada > 9:
                jogo = empate()
                break

            print(tabuleiro)
            sleep(0.5)

            print("PLACAR GERAL: {}".format(placar))
            sleep(1)
            print("Rodada {}".format(rodada))
            sleep(1)
            jogada = int(input("Jogador {}, digite uma posição: ".format(jogador)))
            print("Posição digitada: {}".format(jogada))
            sleep(1)

            if 0 < jogada <= 9:
                if jogada in lista:
                    for c in range(9):
                        if jogada == lista[c]:
                            lista[c] = lista_1[jogador-1]
                            jogador += 1
                            rodada += 1
                        else:
                            c += 1
                else:
                    print("Posição ocupada!")
            else:
                print("Inválido")

    continuar = input("Deseja continuar? S/N: ").upper()

    if continuar == "S":
        jogar = True
        sleep(1)
    else:

        print("PLACAR FINAL: {}  {} x {}  {}.".format(jogador_1, vitorias_1, vitorias_2, jogador_2))
        sleep(1)

        if vitorias_1 > vitorias_2:
            print("{} foi o campeão! Partidas ganhas: {}".format(jogador_1, vitorias_1))
            sleep(1)
            print("{} perdeu! Partidas ganhas: {}".format(jogador_2, vitorias_2))
        elif vitorias_2 > vitorias_1:
            print("{} foi campeão! Partidas ganhas: {}".format(jogador_2, vitorias_2))
            sleep(1)
            print("{} perdeu! Partidas ganhas: {}".format(jogador_1, vitorias_1))
        else:
            print("O jogo terminou empatado!")
            sleep(1)
            print("Obrigado por jogar!")

        jogar = False
