# var_globals.py: Variables globals, com l’amplada del mapa o l’energia inicial.
# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()

vida_jugador = 0
vida_max = 0
animals_restants = 0
pos_jugador = [3, 3] # X, Y
character_jugador = "ඞ"
dificultat = 0 # 0 - FACIL || 1 - MITG || 2 - DIFICIL

#CODI AQUÍ

def RenderText(text, upperText="", delay=0.1):
    from time import sleep
    for i in range(1, len(text)):
        Clear()
        print(upperText)
        print(text[0:i])
        sleep(delay)

def Clear():
    from os import name, system

    if name == "nt":
        system("cls")
    else:
        system("clear")