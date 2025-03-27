# mapa.py: Genera el mapa i col·loca els elements. També gestiona les regles de cada element.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()

import var_globals
import elements as E
from random import randint  # Per coŀlocar els element aleatoriament

# Generar el mapa. Retorna una llista de llistes (matriu) amb elements objecte (Animal, caçador, espai buit, llac...)
lx, ly, elements = 0, 0, 0

element_per_defecte = E.default_element

# Actualitzar les variables segons la dificultat

match var_globals.dificultat:
    case 0:
        # OPCIONS PER DIFICULTAT FÀCIL
        lx, ly, elements = 5, 5, [[E.Animal, 2, 0], [E.Cacador, 1, 0], [E.Trampa, 2, 0], [E.Llac, 5, 0], [E.BoscDens, 3, 0]]  
        var_globals.animals_restants = 2
    case 1:
        # OPCIONS PER DIFICULTAT NORMAL
        lx, ly, elements = 10, 10, [[E.Animal, 5, 0], [E.Cacador, 3, 0], [E.Trampa, 10, 0], [E.Llac, 5, 0], [E.BoscDens, 5, 0]]  
        var_globals.animals_restants = 5
    case 2:
        # OPCIONS PER DIFICULTAT DIFÍCIL
        lx, ly, elements = 15, 15, [[E.Animal, 10, 0], [E.Cacador, 5, 0], [E.Trampa, 25, 0], [E.Llac, 5, 0], [E.BoscDens, 7, 0]]
        var_globals.animals_restants = 10

# X i Y son les dimensions. "Elements" és una matriu, on cada fila té l'element i el nombre d'ocurrences.
# Estan aqui per si hem de fer debug

# Exemple: x=5, y=5, elements=[ [elements.Animal, 10], [elements.Bosc, 5], [elements.Llac, 10] ]
def GenerarMapa(x=lx, y=ly, llista_elements=elements):
    # print("DEBUG: mapa.py MAP DIMENSIONS:", x, y)
    mapa = [[element_per_defecte() for i in range(x)] for j in range(y)]  # Prepara el mapa, amb elements per defecte (Hauria de ser Vacuum)

    # Ara coŀlocar els elements aleatoriament en caselles buides. OJO: SI HI HAN MÉS ELEMENTS QUE CASELLES DISPONIBLES, ENTRARÀ EN BUCLE INFINIT
    for elementInfo in llista_elements:
        element, ocurrences = elementInfo[0], elementInfo[1]
        for i in range(ocurrences):
            rax, ray = randint(0, x) - 1, randint(0, y) - 1
            print(f"DEBUG: trying to put element on {rax};{ray};")
            while type(mapa[ray][rax]) != element_per_defecte or [rax, ray] == var_globals.pos_jugador:
                rax, ray = randint(0, x - 1), randint(0, y - 1)  # Seleccionar una casella buida a l'atzar

            # si es tracta d'un mod, ha de fer servir les energies personalitzades, si no, les que hi ha per defecte
            if elementInfo[2] != 0:
                # L'estructura de la llista d'elements és diferent en els mods; a part de la quantitat, també s'afegeix l'energia
                mapa[ray][rax] = element(energia=elementInfo[2])
            else:
                mapa[ray][rax] = element()
            print("DEBUG: ELEMENT COĿLOCAT")

    return mapa

def GenerarFOW(x=lx, y=ly, character="#"):
    return [[character for i in range(x)] for j in range(y)]  # Retorna la FOW, idealment del mateix tamany que el mapa

def RenderitzarMapa(mapa, fow):
    # Retornarà una string en lineas, amb el mapa generat.
    x, y = len(mapa[0])-1, len(mapa)-1
    # print("DEBUG: IMPRIMINT MAPA--------")
    buffer = ": "

    for i in range(x+1):
        for j in range(y+1):
            if [i, j] == var_globals.pos_jugador:
                buffer += var_globals.character_jugador + " "
                continue

            if fow[j][i] == 0:
                buffer += str(mapa[j][i])
            else:
                buffer += fow[j][i]
            buffer += " "
        buffer += "\n: "

    return buffer
