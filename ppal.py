

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
# import elements as E # Només cal importar-lo si es carregua un mod, pel que es carregua més abaix




# PANTALLA PRINCIPAL, SELECCIONAR DIFICULTAT
# TAMBÉ ES POT SELECCIONAR EL NOM (Funcionalitat extra)
print("Voldrieu carregar els mods?")
print("Si no esteu segurs, seleccioneu \"N\"")
mods = input("Carreguar mods [y/N]:")

if mods.lower() in "yes" and mods!="":
    var_globals.mods_disponibles = var_globals.getMods()
    var_globals.mods_activats = True



missatge_benvilguda = '''

======BENVOLGUTS AL PROJECTE======

BB   EEE  SSS TTTTT III  AA   L
B B  E   S      T    I  A  A  L
BB   EE   SS    T    I  AAAA  L
B B  E      S   T    I  A  A  L
BB   EEE SSS    T   III A  A  LLLL

Dificultats:
1. Fàcil
2. Normal
3. Difícil

'''


mods_seleccio = {}
if var_globals.mods_activats:
    missatge_benvilguda += ("\nMods disponibles:" if len(var_globals.mods_disponibles)!=0 else "No s'han detectat mods disponibles.")

    # Afegeix a la llista "mods_selecció" un parell clau-valor, amb la clau "m{numero del mod}" i valor el nom del mod
    for number, modname in enumerate(var_globals.mods_disponibles):
        mods_seleccio[f"m{number+1}"] = modname
        missatge_benvilguda += f"\nm{number+1}. {modname}"
    print()

#       Demanar la dif, entre 1 i 3. Al acabar, elimina la variable per estalviar espai
#       Codi vell, el nou suporta els mods
#       user = input("Selecció:")
#       while user not in ("1","2","3"):
#           user = input("Selecció fora de rang, prova de nou:")
#       var_globals.dificultat = int(user) - 1
#       del user
#       var_globals.vida_jugador = var_globals.vida_max[var_globals.dificultat]


selecting = True # Mentres l'usuari no seleccioni una dificultat definitiva, fes el bucle
modmenu = False
modname = ""

while selecting:

    # Si l'usuari no és al menu d'un mod
    if not modmenu:

        print(missatge_benvilguda)
        user = input("Selecció:").lower()
        while not (user in ("1","2","3") or user in mods_seleccio):
            print("Error: selecció fora de rang, prova de nou.")
            user = input("Selecció:").lower()
        if user[0]=="m":
            modname = mods_seleccio[user]
            modmenu = True
        else:
            var_globals.dificultat = int(user)-1
            var_globals.vida_max = var_globals.vida_max[int(user)-1]
            selecting = False


    else: # Si l'usuari és al menu d'un mod
        var_globals.Clear()
        seleccionables = {}
        dificultats, energies, banner = var_globals.loadMod(modname)

        print(banner, "\n"*2 + "Dificultats:")
        for number, name in enumerate(dificultats):
            print(f"{number+1}. {name}")
            seleccionables[str(number+1)] = name
        
        user = input("Selecciona la dificultat (Qualsevol valor no acceptable tornarà al menu principal):")
        if user not in seleccionables:
            modmenu = False
        else:
            # Prepara la configuració del mapa del mod seleccionat
            nomDificulat = seleccionables[user]
            info = dificultats[nomDificulat]
            var_globals.dificultat = int(user)-1

            mapaX = info["y"]
            mapaY = info["x"]
            fow_r = info["fow"]
            var_globals.animals_restants_mod = info["goal"]
            var_globals.vida_max = info["hp"]


            import elements as E

            elemsInfo = info["elems"]
            

            modElements = []
            for name in elemsInfo:
                match name:
                    case "Animal":
                        print(energies["Animal"], var_globals.dificultat)
                        modElements.append([E.Animal, elemsInfo["Animal"], energies["Animal"][var_globals.dificultat]])
                    case "Cacador":
                        modElements.append([E.Cacador, elemsInfo["Cacador"], energies["Cacador"][var_globals.dificultat]])
                    case "BoscDens":
                        modElements.append([E.BoscDens, elemsInfo["BoscDens"], energies["BoscDens"][var_globals.dificultat]])
                    case "Llac":
                        modElements.append([E.Llac, elemsInfo["Llac"], energies["Llac"][var_globals.dificultat]])
                    case "Trampa":
                        modElements.append([E.Trampa, elemsInfo["Trampa"], energies["Trampa"][var_globals.dificultat]])

            selecting = False # Surt del menu principal i comença el joc
        
        var_globals.Clear() # Neteja la pantalla per fer espai al banner del mod






var_globals.Clear() # fer una mica d'espai

#DEBUG: TEST IF DIFFICULTY SET CORRECTLY

#print("DEBUG: DIFICULTY:", var_globals.dificultat)


import mapa, moviments # La resta les importem aquí, així algunes configuracions no es desincronitzen (No llegeixin la dificultat abans de seleccionar-la)
import elements as E

if var_globals.animals_restants_mod != 0: var_globals.animals_restants = var_globals.animals_restants_mod


if modmenu:
    var_globals.mapa = mapa.GenerarMapa(x=mapaX, y=mapaY, llista_elements=modElements)
    map = var_globals.mapa
    FOW = mapa.GenerarFOW(x=mapaX, y=mapaY,character="#")
else:
    var_globals.mapa = mapa.GenerarMapa()
    map = var_globals.mapa

    FOW = mapa.GenerarFOW(character="X") # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa
    fow_distancies = [2, 1.5, 1]
    fow_r = fow_distancies[var_globals.dificultat]


#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)

playing = True # Serà False quan la partida termini.
var_globals.vida_jugador = var_globals.vida_max
while playing:
    var_globals.Clear() # Donar espai pq la terminal quedi netal2


    moviments.UpdateFOW(FOW, fow_r)
    print(f"Vida del jugador: {var_globals.vida_jugador} / {var_globals.vida_max}")
    print(mapa.RenderitzarMapa(map, FOW))
    print(f"Animals restants: {var_globals.animals_restants}")



    moviments.moure(input("Selecciona el teu moviment:"), map)
    

    
    if var_globals.vida_jugador <= 0:
        playing = False
        print("💀 Has perdut! T'has quedat sense energia!")

    if var_globals.animals_restants == 0:
        playing = False
        print("🎉 Has fotografiat tots els animals! Has guanyat! 🎉")

    
    


