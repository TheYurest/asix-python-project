#  EEE    EEEE    EEEE   EEEEE   EEEEE    EEE    E
#  E  E   E      E         E       E     E   E   E
#  EEE    EEE     EEE      E       E     EEEEE   E
#  E  E   E          E     E       E     E   E   E
#  EEE    EEEE    EEE      E     EEEEE   E   E   EEEEE

#   AAA   DDDD   IIIII  L
#  A   A  D   D    I    L
#  AAAAA  D   D    I    L
#  A   A  D   D    I    L
#  A   A  DDDD   IIIII  LLLLL


# MÒDUL PRINCIPAL (main.py)
# ppal.py: Mòdul principal que inicialitza el joc i mostra el resultat final.


# ENTREGA PARCIAL:  28 FEB
# ENTREGA FINAL  :  11 ABR

# REQUISITS DEL PROGRAMA (copy-pasta del document) A REQUISITS.TXT





# Importar tots els mòduls adicionals
import var_globals




# PANTALLA PRINCIPAL, SELECCIONAR DIFICULTAT
# TAMBÉ ES POT SELECCIONAR EL NOM (Funcionalitat extra)

print('''

======BENVOLGUTS AL PROJECTE======

BB   EEE  SSS TTTTT III  AA   L
B B  E   S      T    I  A  A  L
BB   EE   SS    T    I  AAAA  L
B B  E      S   T    I  A  A  L
BB   EEE SSS    T   III A  A  LLLL

''')
print("Selecciona la teva dificultat:")
print("1. Fàcil\n2. Normal\n3. Difícil")

# Demanar la dif, entre 1 i 3. Al acabar, elimina la variable per estalviar espai
user = input("Selecció:")
while user not in ("1","2","3"):
    user = input("Selecció fora de rang, prova de nou:")
var_globals.dificultat = int(user) - 1
del user

# Canviar la vida i la vida màxima
energies = [100, 50, 25]
var_globals.vida_jugador = energies[var_globals.dificultat]
var_globals.vida_max = var_globals.vida_jugador


print("\n"*10) # fer una mica d'espai

#DEBUG: TEST IF DIFFICULTY SET CORRECTLY

#print("DEBUG: DIFICULTY:", var_globals.dificultat)


import mapa, moviments # La resta les importem aquí, així algunes configuracions no es desincronitzen (No llegeixin la dificultat abans de seleccionar-la)


map = mapa.GenerarMapa()
FOW = mapa.GenerarFOW(character=0) # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa



#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)

playing = True # Serà False quan la partida termini.

while playing:
    print(f"{var_globals.vida_jugador}/{var_globals.vida_max} ♥ ------ Sitting on: {map[var_globals.pos_jugador[1]][var_globals.pos_jugador[0]]}. Coords: {var_globals.pos_jugador}")
    print(mapa.RenderitzarMapa(map, FOW))
    print(f"Cell energy: {map[var_globals.pos_jugador[1]][var_globals.pos_jugador[0]].energia}")
    moviments.moure(input("Selecciona el teu moviment:"), map)


    print("\n"*25) # Donar espai pq la terminal quedi neta

