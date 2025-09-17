import os
import random
from colorama import Fore, Back, Style
jogarNovamente = "s"
jogadas = 0
quemJoga = 1 # 1 - Jogador ; 2 - CPU
maxJogadas = 9
vit = False
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def interface():
   global velha
   global jogadas
   os.system("clear")
   print("    0   1   2")
   print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
   print("   ------------")
   print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
   print("   ------------")
   print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
   print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogadaPlayer():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas<maxJogadas:
        linha = int(input("Linha..:"))
        coluna = int(input("Coluna:"))
        while velha[linha][coluna] != " ":
            linha = int(input("Linha..:"))
            coluna = int(input("Coluna:"))
        try:
            velha[linha][coluna] = "O"
            quemJoga = 2
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida")


def jogadaCPU():
    global jogadas
    global quemJoga
    global maxJogadas
    l = random.randint(0,2)
    c = random.randint(0,2)
    if velha[l][c] != " ":
        while velha[l][c] != " ":
            l = random.randint(0,2)
            c = random.randint(0,2)
        velha[l][c] = "X"
        jogadas+=1
        quemJoga = 1
 


def verificarVitoria():
    global velha
    vitoria = "n"
    for i in range(3):
        if velha[i][0] == velha[i][1] == velha[i][2] and velha[i][0] != " ":
            vitoria = "s"
            return True
        
    for j in range(3):
        if velha[0][j] == velha[1][j] == velha[2][j] and velha[0][j] != " ":
            vitoria = "s"
            return True
        
    if velha[0][0] == velha[1][1] == velha[2][2] and velha[0][0] != " ":
        vitoria = "s"
        return True
    
    if velha[0][2] == velha[1][1] == velha[2][0] and velha[0][2] != " ":
        vitoria = "s"
        return True

    vitoria = "n"
    return False 


def verificarEmpate():
    global velha
    for linha in velha:
        for celula in linha:
            if celula == " ":
                return False  
    return True 

def reiniciarJogo():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    jogadas = 0
    quemJoga = 1
    maxJogadas = 9
    for i in range(3):
        for j in range(3):
            velha[i][j] = " "


def jogarNovamenteFuncao():
    global jogarNovamente
    while True:
        jogarNovamente = input("Deseja jogar novamente? [s/n]").lower()
        if jogarNovamente == "s":
            reiniciarJogo()
            jogo()
            break
        elif jogarNovamente == "n":
            print("Encerrando...")
            break
        else:
            print("Resposta Inválida. Digite 's' ou 'n'.")

def jogo():
    while True:
        interface()
        jogadaPlayer()

        if verificarVitoria():
            print("Parabéns, você venceu!") 
            jogarNovamenteFuncao()
            break

        elif verificarEmpate():
            print("DEU empate")
            jogarNovamenteFuncao()
            break

        jogadaCPU()
        if verificarVitoria():
            print("O computador venceu!") 
            jogarNovamenteFuncao()
            break
        elif verificarEmpate():
            print("DEU empate")
            jogarNovamenteFuncao()
            break

jogo()
