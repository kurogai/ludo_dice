import random
import time

#vai chamar essa funcao se tirarmos um 6 com um dado [completo]
def _dado1(dado1, nome):
    print("\033[1;37m[{}] Tiraste 6 com um dado, girando...\033[m".format(nome))
    dado1 = random.randint(1,6)
    time.sleep(2)
    if dado1 == 6:
        return _dado1(dado1,nome)
    else:
        print("\033[1;37m[dado1] => {}\033[m".format(dado1))
        return

#vai chamar esta funcao se tirarmos 6 com os dois dados
def _dado2(dado1, dado2,nome):
    print("\033[1;37m[{}] Tiraste 6 com os dois dados\033[1;37m".format(nome))
    time.sleep(2)
    
    dado1,dado2 = random.randint(1,6), random.randint(1,6)

    #-------------------ja sabemos------------------------
    if (dado1 != 6 and dado2 != 6) and (dado1 != dado2):
        print("\033[1;37m[!] Dado1 => {} | dado2 => {}\033[m".format(dado1,dado2))
        return
    if dado1 == 6 and dado2 == 6:
        return _dado2(dado1,dado2,nome)
    elif dado1 == 6 and dado2 != 6:
        print("\033[1;37m[!] Tiraste 6 com o primeiro dado, o segundo deu {}\033[m".format(dado2))
        q = dado1
        _dado1(q,nome)
    elif dado1 != 6 and dado2 == 6:
        print("\033[1;37m[!] Tiraste 6 com o segundo dado, o primeiro deu {}\033[m".format(dado1))
        q = dado2
        _dado1(q,nome)
    #-------------------Ja sabemos

#vai chamar esta funcao se os dados forem iguais
def _iguais(dado1,dado2,nome):
    print("\033[1;31m[{}] Tiraste dados iguais => {} | {}\033[m".format(nome,dado1,dado2))
    time.sleep(2)

    dado1,dado2 = random.randint(1,6), random.randint(1,6)

    if (dado1 != 6 and dado2 != 6) and (dado1 != dado2):
        print("\033[1;37m[!] Dado1 => {} | dado2 => {}\033[m".format(dado1,dado2))
        return
    if dado1 == dado2:
        return _iguais(dado1,dado2,nome)
    if dado1 == 6 and dado2 != 6:
        print("\033[1;37m[!] Tiraste 6 com o primeiro dado, o segundo deu {}\033[m".format(dado2))
        q = dado1
        _dado1(q,nome)
    elif dado1 != 6 and dado2 == 6:
        print("\033[1;37m[!] Tiraste 6 com o segundo dado, o primeiro deu {}\033[m".format(dado1))
        q = dado2
        _dado1(q,nome)
    if dado1 == 6 and dado2 == 6:
         _dado2(dado1,dado2,nome)


def main():
    players = "\033[1;35mJogador1\033[m","\033[1;32mJogador2\033[m","\033[1;33mJogador3\033[m","\033[1;34mJogador4\033[m"
    x = 0
    q = 0
    #loop infinito ate o jogo terminar
    try:
        while True:
            while x < len(players):
                input("\033[1;37m[!] De enter para girar... > \033[m")
                dado1,dado2 = random.randint(1,6), random.randint(1,6)
                print("\033[1;37m[{}] => {} | {}\033[m".format(players[x], dado1, dado2))

                #-------------------------Um deles for 6----------------------
                if dado1 == 6 and dado2 != 6:
                    q = dado1
                    _dado1(q,players[x])
                elif dado1 != 6 and dado2 == 6:
                    q = dado2
                    _dado1(q,players[x])
                #-------------------------------------------------------------
                elif dado1 == 6 and dado2 == 6:
                    _dado2(dado1,dado2,players[x])

                elif dado1 == dado2:
                    _iguais(dado1,dado2,players[x])

                #time.sleep(1)
                x = x+1
            x = 0
    except KeyboardInterrupt:
        print("\033[1;37m[!] Saindo do jogo...\033[m")
        return

if __name__ == "__main__":
    main()
