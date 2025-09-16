import os
import random
from colorama import Fore, Back, Style
# def jogadaJogador, jogadaCPU, verificarVitoria, redefinir para jogar novamente
jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vitoria = False
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
    linha = int(input("Linha..:"))
    coluna = int(input("Coluna:"))
    velha[linha][coluna] = "O"

def jogadaCPU():
    l = random.randint(0,2)
    c = random.randint(0,2)
    while velha[l][c] == "O":
        if velha[l][c] == "O":
            l = random.randint(0,2)
            c = random.randint(0,2)
        else:
            velha[l][c] = "X"
            break

def verificarVitoria():
    

#while True:
interface()
jogadaPlayer()
interface()
    # jog
    # cpu
    # vv