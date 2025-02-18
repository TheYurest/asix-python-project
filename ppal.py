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


#  K  K   AAA   NN   N   AAA   V   V
#  K K   A   A  N N  N  A   A  V   V
#  KK    AAAAA  N  N N  AAAAA   V V
#  K K   A   A  N   NN  A   A   V V
#  K  K  A   A  N    N  A   A    V


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
print("\n"*10) # fer una mica d'espai

#DEBUG: TEST IF DIFFICULTY SET CORRECTLY

#print("DEBUG: DIFICULTY:", var_globals.dificultat)


import mapa, moviments # La resta les importem aquí, així algunes configuracions no es desincronitzen (No llegeixin la dificultat abans de seleccionar-la)


map = mapa.GenerarMapa()
FOW = mapa.GenerarFOW(character=0) # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa



#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)

playing = True # Serà False quan la partida termini.

while playing:
    print(mapa.RenderitzarMapa(map, FOW))
    moviments.moure(input("Selecciona el teu moviment:"), map)
    print("\n"*25) # Donar espai pq la terminal quedi netal2
    

