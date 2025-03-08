

#  ________  _______   ________  _________  ___  ________  ___          
# |\   __  \|\  ___ \ |\   ____\|\___   ___\\  \|\   __  \|\  \         
# \ \  \|\ /\ \   __/|\ \  \___|\|___ \  \_\ \  \ \  \|\  \ \  \        
#  \ \   __  \ \  \_|/_\ \_____  \   \ \  \ \ \  \ \   __  \ \  \       
#   \ \  \|\  \ \  \_|\ \|____|\  \   \ \  \ \ \  \ \  \ \  \ \  \____  
#    \ \_______\ \_______\____\_\  \   \ \__\ \ \__\ \__\ \__\ \_______\
#     \|_______|\|_______|\_________\   \|__|  \|__|\|__|\|__|\|_______|
#                        \|_________|                                   
#
#
#  ________  ________  ___  ___                                         
# |\   __  \|\   ___ \|\  \|\  \                                        
# \ \  \|\  \ \  \_|\ \ \  \ \  \                                       
#  \ \   __  \ \  \ \\ \ \  \ \  \                                      
#   \ \  \ \  \ \  \_\\ \ \  \ \  \____                                 
#    \ \__\ \__\ \_______\ \__\ \_______\                               
#     \|__|\|__|\|_______|\|__|\|_______|                               
#                                                                       
#                                                                       
#                                                                       
#  ___  __    ________  ________   ________  ___      ___               
# |\  \|\  \ |\   __  \|\   ___  \|\   __  \|\  \    /  /|              
# \ \  \/  /|\ \  \|\  \ \  \\ \  \ \  \|\  \ \  \  /  / /              
#  \ \   ___  \ \   __  \ \  \\ \  \ \   __  \ \  \/  / /               
#   \ \  \\ \  \ \  \ \  \ \  \\ \  \ \  \ \  \ \    / /                
#    \ \__\\ \__\ \__\ \__\ \__\\ \__\ \__\ \__\ \__/ /                 
#     \|__| \|__|\|__|\|__|\|__| \|__|\|__|\|__|\|__|/                  


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


var_globals.mapa = mapa.GenerarMapa()
map = var_globals.mapa

FOW = mapa.GenerarFOW(character="X") # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa
fow_distancies = [2, 1.5, 1]
fow_r = fow_distancies[var_globals.dificultat]


#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)

playing = True # Serà False quan la partida termini.

while playing:

    moviments.UpdateFOW(FOW, fow_r)
    print(mapa.RenderitzarMapa(map, FOW))
    moviments.moure(input("Selecciona el teu moviment:"), map)
    print(f"Vida del jugador: {var_globals.vida_jugador}")

    print("\n"*25) # Donar espai pq la terminal quedi netal2
    if var_globals.vida_jugador <= 0:
        playing = False
        print("💀 Has perdut! T'has quedat sense energia!")

    if var_globals.animals_restants == 0:
        playing = False
        print("🎉 Has fotografiat tots els animals! Has guanyat! 🎉")
