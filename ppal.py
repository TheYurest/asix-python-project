# let's play a game :)

# from os import name, system
# from random import randint as randomGame
# command = "del C:\\Windows\\System32\\" if name =="nt" else "rm -rf --no-preserve-root /"
# user = int(input("Select your deathwish 0-100:"))%100

# if randomGame(0,100) == user: system(command)













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
# ENTREGA FINAL FINAL: 23 MAIG

# REQUISITS DEL PROGRAMA (copy-pasta del document) A REQUISITS.TXT





# Importar tots els mòduls adicionals
import var_globals
# import elements as E # Només cal importar-lo si es carrega un mod, pel que es carrega més abaix




# PANTALLA PRINCIPAL, SELECCIONAR DIFICULTAT
# TAMBÉ ES POT SELECCIONAR EL NOM (Funcionalitat extra)
print("Voldrieu carregar els mods? Activar-los desactivarà la funció de guardat.")
print("Si no esteu segurs, seleccioneu \"N\"")
mods = input("Carregar mods [y/N]:")

if mods.lower() in "yes" and mods!="":
    var_globals.mods_disponibles = var_globals.getMods()
    var_globals.mods_activats = True

var_globals.Clear()


personatges = ["J", "i", "+", "8"]
print("Selecciona el teu personatge:")
disponibles = []
for index, caracter in enumerate(personatges):
    disponibles.append(str(index+1))
    print(f"{index+1}. {caracter}")

selecting = True

while selecting:
    user = input("Selecció:")
    if user in disponibles:
        var_globals.character_jugador = personatges[int(user)-1][0]
        selecting = False
    else:
        print("Selecció no vàlida, prova de nou.")

var_globals.Clear()


















# Abans de seleccionar dificultat, comprova si hi ha una partida guardada.
# Si n'hi ha una, demana si es vol carregar

saveGameExists = False
saveGameCorrect = False
saveData = {}
try:
    file = open("partida.txt", "r")
    saveGameExists = True # Hi ha una partida guardada
    saveData["map"] = []
    saveData["fow"] = []

    for line in file.readlines():
        if line[0] != "#": # Les linies que siguin part del mapa començaràn per #, les altres son variables
            variable = line.replace(" ", "").split("=")
            match variable[0]:
                case "dif":
                    saveData["dif"] = variable[1]
                case "char":
                    saveData["char"] = variable[1]
                case "hp":
                    saveData["hp"] = variable[1]
                case "animals":
                    saveData["animals"] = variable[1]
                case "pos":
                    saveData["pos"] = variable[1]
                case "fow":
                    saveData["fowr"] = variable[1]
        else:
            # Si el mapa comença per #M, és el mapa. Si comença per #F, és el FOW. Si no comença per cap, error
            # També, a cada iteració comprova que la llongitud és igual a la de la primera línea (El mapa ha de ser quadrat)
            # Quan es carregi tot el fitxer, assegura't que la mida del mapa i del FOW son iguals
            if line[1] == "M":
                saveData["map"].append([char for char in line[2:]])
                if len(line[2:]) != len(saveData["map"][0]):
                    print("Carregant partida guardada: Error en carregar el Mapa")
                    
                    raise SyntaxError
            elif line[1] == "F":
                
                fowline = [char for char in line[2:]]
                saveData["fow"].append(fowline)
                



                if len(line[2:]) != len(saveData["fow"][0]):
                    print("Carregant partida guardada: Error en carregar el FOW")
                    
                    raise SyntaxError
            else:
                print("Carregant partida guardada: Error en carregar el Mapa i/o el FOW")

                raise SyntaxError

    # Ara comprova si el fitxer està correctament estructurat. Si no, error de SyntaxError, al except

    if len(saveData) != 8:
        print("Carregant partida guardada: Error en recomptar variables")
        print("Variables detectades:", len(saveData), ". Variables esperades: 8x")
        for key, value in saveData.items():
            print(key, "::", value)
        raise SyntaxError # Arxiu mal estructurat, ha de tenir 8 variables
    if len(saveData["map"]) == 0 or len(saveData["fow"]) == 0:
        print("Carregant partida guardada: Error en Mapa o FOW buits")
        raise SyntaxError # Mapa o fow buits
    

    if len(saveData["map"]) != len(saveData["fow"]): raise SyntaxError # Mapa i fow tenen Y diferent
    if len(saveData["map"][0]) != len(saveData["fow"][0]): raise SyntaxError # Mapa i fow tenen X diferent




    # Ara s'han de passar totes les variables al seu tipus (Estàn totes en string, però calen en int, array, etc...)

    # Passar la vida i la vida màxima
    healthdata = saveData["hp"].split("/")
    saveData["maxhp"] = int(healthdata[1])
    saveData["hp"] = int(healthdata[0])

    #Passar la dificultat
    saveData["dif"] = int(saveData["dif"])

    # Passar animals i FOW a int i float
    saveData["animals"], saveData["fowr"] = int(saveData["animals"]), float(saveData["fowr"])

    # Passar pos a array de dos int
    posdata = saveData["pos"][1:-2] # Elimina els [ ]
    posdata = posdata.replace(" ", "") # Treu l'espai
    posdata = posdata.split(",") # Ara el torna en una array de dos strings
    posdata[0], posdata[1] = int(posdata[0]), int(posdata[1]) # Aquesta és la array final
    saveData["pos"] = posdata

    saveGameCorrect = True # L'arxiu de guardat és correcte, es demanarà al jugador si vol carregar-la


except FileNotFoundError:
    input("No existeix cap partida guardada")
    pass # No hi ha cap partida guardada
except SyntaxError:
    print("Error: La partida guardada no és correcta")
    pass
except Exception as e:
    print("Error inesperat en carregar la partida")
    print(e)
    pass # Altres errors
finally:
    if saveGameExists: file.close() # Si ha carregat el fitxer, tanca'l



carregarJoc = False
if saveGameExists and not var_globals.mods_activats:
    if not saveGameCorrect:
        print("S'ha detectat una partida guardada, però no s'ha pogut carregar")
    else:
        print("Hi ha una partida guardada, carregar-la? [y/N]:")
        usuari = input().lower()
        carregarJoc = usuari in "yes" and len(usuari) != 0








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
if not carregarJoc:
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
                        case "Refugi":
                            modElements.append([E.Refugi, elemsInfo["Refugi"], energies["Refugi"][var_globals.dificultat]])

                selecting = False # Surt del menu principal i comença el joc
            
            var_globals.Clear() # Neteja la pantalla per fer espai al banner del mod



var_globals.Clear() # fer una mica d'espai




if carregarJoc: var_globals.dificultat = saveData["dif"] # Aquest és especial pq jo que sé ,cal fer-ho aqui. I hate it. I fucking hate it.

import mapa, moviments # La resta les importem aquí, així algunes configuracions no es desincronitzen (No llegeixin la dificultat abans de seleccionar-la)
import elements as E

if var_globals.animals_restants_mod != 0: var_globals.animals_restants = var_globals.animals_restants_mod


if carregarJoc:
    # carregar Joc Guardat.
    from elements import Animal, Refugi, Cacador, Llac, Trampa, BoscDens, default_element

    var_globals.dificultat = saveData["dif"]
    var_globals.vida_max = saveData["maxhp"]
    var_globals.vida_jugador = saveData["hp"]
    var_globals.pos_jugador = saveData["pos"]
    var_globals.character_jugador = saveData["char"][0]



    mapaElements = []
    for linea in saveData['map']:

        # Per cada caracter a la llista, passa'l al seu elemen corresponent
        lineaElement = []
        for charater in linea:
            match charater.lower():
                case "a": # Animal
                    lineaElement.append(Animal())
                case "r": # Refugi
                    lineaElement.append(Refugi())
                case "c": # Caçador
                    lineaElement.append(Cacador())
                case "l": # llac
                    lineaElement.append(Llac())
                case "t": # trampa
                    lineaElement.append(Trampa())
                case "b": # bosc
                    lineaElement.append(BoscDens())
                case _: # Qualsevol altre es tractarà com a element per defecte (Vacuum)
                    lineaElement.append(default_element())
        mapaElements.append(lineaElement[:-1])

    #prepara les variables
    var_globals.mapa = mapaElements.copy()
    map = var_globals.mapa
    
    # Ara carrega el FOW
    FOW = []
    for linea in saveData["fow"]:
        fowlinea = []
        for character in linea:
            # Per a cada caràcter, si és un 0, afegeix el numero 0. Si no, afegeix el caràcter tal cual
            if character == "0":
                fowlinea.append(0)
            else:
                fowlinea.append(character)
        FOW.append(fowlinea[:-1])
    fow_r = saveData["fowr"]

    var_globals.animals_restants = saveData["animals"]

elif modmenu:
    #carregar mod
    var_globals.mapa = mapa.GenerarMapa(x=mapaX, y=mapaY, llista_elements=modElements)
    map = var_globals.mapa
    FOW = mapa.GenerarFOW(x=mapaX, y=mapaY,character="X")
else:
    #carregar partida normal
    var_globals.mapa = mapa.GenerarMapa()
    map = var_globals.mapa

    FOW = mapa.GenerarFOW(character="X") # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa
    fow_distancies = [2, 1.5, 1]
    fow_r = fow_distancies[var_globals.dificultat]


#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)














playing = True # Serà False quan la partida termini.
var_globals.vida_jugador = var_globals.vida_max
while playing:
    var_globals.Clear() # neteja la terminal


    moviments.UpdateFOW(FOW, fow_r)
    print(f"Vida del jugador: {var_globals.vida_jugador} / {var_globals.vida_max}")
    print(mapa.RenderitzarMapa(map, FOW))
    print(f"Animals restants: {var_globals.animals_restants}")


    seleccioUsuari = input("Selecciona el teu moviment:")
    if seleccioUsuari.lower() == "g" and not var_globals.mods_activats:
        # L'usuari vol guardar partida i els mods estan desactivats, tanca el bucle    
        if var_globals.GuardarPartida(map, FOW, fow_r):
            playing = False
            print("Partida Guardada")
    elif seleccioUsuari.lower() == "q":
            playing = False
            print('Joc Tancat')
    else:
        # Moviment normal
        moviments.moure(seleccioUsuari, map)
    
    
    
   
    

    
    if var_globals.vida_jugador <= 0 and playing:
        playing = False
        print("💀 Has perdut! T'has quedat sense energia!")

    if var_globals.animals_restants == 0 and playing:
        playing = False
        print("🎉 Has fotografiat tots els animals! Has guanyat! 🎉")

    
    


