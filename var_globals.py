# var_globals.py: Variables globals, com l’amplada del mapa o l’energia inicial.
# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()

vida_jugador = 0
vida_max = 0
animals_restants = 0
pos_jugador = [3, 3] # X, Y
character_jugador = "E"
dificultat = 0 # 0 - FACIL || 1 - MITG || 2 - DIFICIL

#CODI AQUÍ

def RenderText(text, upperText="", delay=0.1, s=1):

    while delay < 0.01:
        delay *=2
        s *= 2

    from time import sleep
    for i in range(1, len(text)+1, s):
        Clear()
        print(upperText)
        print(text[0:i])
        sleep(delay)
    Clear()
    print(upperText)
    print(text)

def Wait(seconds):
    from time import sleep
    sleep(seconds)


def Credits():

    credits= r'''
_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_
Programació: Adil Challali Hidalgo

Art: asciiart.eu (Cada imatge té la firma acreditada)
Fonts: asciiart.eu (Fets amb l'eina "text to ascii")
_,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,__,.-'~'-.,_
'''

    titol = r'''
/==========================================================\
||                                                        ||
||   ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗  ||
||  ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝  ||
||  ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗  ||
||  ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║  ||
||  ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║  ||
||   ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝  ||
||                                                        ||
\==========================================================/
'''


    Clear()
    RenderText(credits, titol, 0.1, 6)

def Clear():
    from os import name, system

    if name == "nt":
        system("cls")
    else:
        system("clear")