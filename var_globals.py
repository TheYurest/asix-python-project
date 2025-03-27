# var_globals.py: Variables globals, com l’amplada del mapa o l’energia inicial.
# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()

vida_jugador = 99
vida_max = [100, 50, 25]
mapa = None  # Initialize the map variable


pos_jugador = [3, 3] # X, Y
character_jugador = "ඞ"
dificultat = 0 # 0 - FACIL || 1 - MITG || 2 - DIFICIL
animals_restants = 0
animals_restants_mod = 0




# Apartat que s'encarregua dels mods
from pathlib import Path
from json import loads, decoder

mods_disponibles = [] # Llista amb els mods correctament estructurats
mods_activats = False

def getMods():

    #Aquesta funció retornarà una llista de strings amb els noms dels mods disponibles i que no tenen errors
    
    detectats = [mod.name for mod in Path("mods").iterdir() if mod.is_dir()] # Llista de strings amb els mods detectats
    print("Detected mods:", *detectats, end="")
    input()
    print("\n"*2)

    disponibles = [] # Llista dels mods que estan correctament escrits
    for mod in detectats:
        modpath = f"mods/{mod}"
        # Comprova que cada mod estigui ben formatat.

        #Primer, comprova si els arxiu obligatoris existeixen. Si no existeixen, passa del mod
        if not (Path.exists(Path(f"{modpath}/modinfo.json")) and Path.exists(Path(f"{modpath}/defaults.json"))): 
            print(f"Mod {mod} couldn't be loaded.")
            continue

        # Intenta carreguar els arxius obligatoris, i si estan ben estructurats
        try:
            modinfo = loads(open(f"{modpath}/modinfo.json","r").read())
            print(f"{mod} modinfo loaded successfully")

            defaults = loads(open(f"{modpath}/defaults.json","r").read())
            print(f"{mod} defaults loaded successfully")

            
            
            # Comprova l'arxiu modinfo, i guarda la informació del mod
            modname=str(modinfo["name"])
            moddescription=str(modinfo["description"])
            modauthor="Anon" if not "author" in modinfo else str(modinfo["author"])
            modversion="none" if not "version" in modinfo else str(modinfo["version"])
            modbanner="" if not "banner" in modinfo else str(modinfo["banner"])



            # Ara comprova l'arxiu defaults, i guarda la seva informació
            modmaxhp=defaults["maxHP"]
            modanimal=defaults["Animal"]
            modcacador=defaults["Cacador"]
            modtrampa=defaults["Trampa"]
            modllac=defaults["Llac"]
            modboscdens=defaults["BoscDens"]

            # Tots els elements han de ser int, així que comproval's tots
            for i in [*modmaxhp, *modanimal, *modcacador, *modtrampa, *modllac, *modboscdens]:
                if not isinstance(i, int): raise TypeError # Si qualsevol del elements no és un int, salta error TypeError

            # Ara, comprova l'arxiu difs.json
            difs = loads(open(f"mods/{mod}/difs.json","r").read())

            #Aquesta funció retorna True si la dificultat está ben estructurada i és vàlida. Si no, retorna False
            def checkdif(difficulty):
                if difficulty["x"] <=0 or difficulty["y"] <=0 or difficulty["goal"] <=0 or difficulty["fow"] < 0 or difficulty["hp"] <=0: return False # els valors han de ser positius
                difelements = difficulty["elems"]
                for element, quantitat in difelements.items():
                    if not (isinstance(quantitat, int) and isinstance(element, str)): return False
                #FIXME: Aquesta funció segurament no està acabada, pot passar qualsevol cosa
                return True
            
            #Ara, itera sobre totes les dificultats, i comprova que totes estiguin ben fetes:
            for dificultat in difs:
                if not checkdif(difs[dificultat]): raise SyntaxError # Si una dificultat està malament estructurada, passa del mod
            
            print(f"Dificultats del mod {mod} carreguades correctament")

            # Aquí es controŀlen els errors
        except decoder.JSONDecodeError:
            print(f"ERROR: El mod {mod} no s'ha pogut decodificar amb json")
            continue
        except KeyError:
            print(f"ERROR: El mod {mod} No està correctament estructurat")
        except TypeError:
            print(f"ERROR: El mod {mod} conté valors incorrectes")
        except:
            print(f"ERROR INESPERAT: El mod {mod} té un error inesperat")
        else:
            disponibles.append(mod) # Si no hi ha cap error, marca el mod com a disponible
            #(OJO: NO CARREGUA EL MOD, NOMÉS L'AFEGEIX A LA LLISTA DE MODS DISPONIBLES. EL MOD ES CARREGUARÀ QUAN ES SELECCIONI)
        
        return disponibles

    print("DEBUG: Mods disponibles:", *disponibles)



# Ara una funció que retorna les dificultats d'un mod, donat el seu nom
def loadMod(modname):
    banner = loads(open(f"mods/{modname}/modinfo.json","r").read())["banner"]
    difs = {}
    mod = loads(open(f"mods/{modname}/difs.json","r").read())
    for difname in mod:
        difs[difname] = mod[difname]
    return difs, banner
    