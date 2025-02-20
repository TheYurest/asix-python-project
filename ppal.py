#  ___   ____  __  _____  _    __    _       
# | |_) | |_  ( (`  | |  | |  / /\  | |      
# |_|_) |_|__ _)_)  |_|  |_| /_/--\ |_|__    
#   __    ___   _   _         __    _        
#  / /\  | | \ | | | |       / /`  | |_|  __ 
# /_/--\ |_|_/ |_| |_|__     \_\_, |_| | (_()
# asciiart.eu


# MÒDUL PRINCIPAL (main.py)
# ppal.py: Mòdul principal que inicialitza el joc i mostra el resultat final.


# ENTREGA PARCIAL:  28 FEB
# ENTREGA FINAL  :  11 ABR

# REQUISITS DEL PROGRAMA (copy-pasta del document) A REQUISITS.TXT
if __name__ != "__main__":
    exit("ERROR: ppal.py ha de ser executat com a *main*")



# Importar tots els mòduls adicionals
import var_globals

var_globals.Clear()
print("Atenció: Aquest programa fa servir art ascii, pel que recomanem fer més gran el terminal per millor visualització, i que la font sigui \"monospace\".\n\nHauries de poder entendre aquest text:")
print(r''' ________                                              __           
|        \                                            |  \
| $$$$$$$$ __    __   ______   ______ ____    ______  | $$  ______
| $$__    |  \  /  \ /      \ |      \    \  /      \ | $$ /      \
| $$  \    \$$\/  $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$|  $$$$$$\
| $$$$$     >$$  $$ | $$    $$| $$ | $$ | $$| $$  | $$| $$| $$    $$
| $$_____  /  $$$$\ | $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$| $$$$$$$$
| $$     \|  $$ \$$\ \$$     \| $$ | $$ | $$| $$    $$| $$ \$$     \
 \$$$$$$$$ \$$   \$$  \$$$$$$$ \$$  \$$  \$$| $$$$$$$  \$$  \$$$$$$$
                                            | $$
                                            | $$
                                             \$$''')
print("En aquests casos, podràs polsar [Enter] per continuar, encara que no es demani.")
input("Prem enter per continuar...")




# PANTALLA PRINCIPAL, SELECCIONAR DIFICULTAT
# TAMBÉ ES POT SELECCIONAR EL NOM (Funcionalitat extra)
print("\n"*25)
intro = r'''
        ___  ____ _  _ _  _ _ _    ____ _  _ ___ ____    ____ _       ___  ____ ____  _ ____ ____ ___ ____
        |__] |___ |\ | |  | | |    | __ |  |  |  [__     |__| |       |__] |__/ |  |  | |___ |     |  |___
        |__] |___ | \|  \/  | |___ |__] |__|  |  ___]    |  | |___    |    |  \ |__| _| |___ |___  |  |___
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\                                                                                                    / /\ 
/ /\ \                                                                                                  / /\ \
\ \/ /    ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               \ \/ /
 \/ /    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌               \/ / 
 / /\    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌               / /\ 
/ /\ \   ▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌              / /\ \
\ \/ /   ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌              \ \/ /
 \/ /    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░▌               \/ / 
 / /\    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌          ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░▌               / /\ 
/ /\ \   ▐░▌       ▐░▌▐░▌                    ▐░▌     ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌              / /\ \
\ \/ /   ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌      ▄▄▄▄█░█▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄     \ \/ /
 \/ /    ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     \/ / 
 / /\     ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀      / /\ 
/ /\ \                                                                                                  / /\ \
\ \/ /                                                                                                  \ \/ /
 \/ /                                                                                                    \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 

'''


var_globals.RenderText("Selecciona la teva dificultat:\n1. Fàcil\n2. Normal\n3. Difícil", upperText=intro, delay=0.005)

# Demanar la dif, entre 1 i 3. Al acabar, elimina la variable per estalviar espai
user = input("Selecció:")
while user.lower() not in ("1","2","3"):


    # Si l'usuari vol veure els credits, passar-los i tornar a demanar l'input
    if user.lower() == "credits":
        var_globals.Credits()
        input("Prem enter per continuar...")
        var_globals.Clear()
        var_globals.RenderText("Selecciona la teva dificultat:\n1. Fàcil\n2. Normal\n3. Difícil", upperText=intro, delay=0.005)
        user = input("Selecció:")

    else:
        user = input("Selecció fora de rang, prova de nou:")
var_globals.dificultat = int(user) - 1
del user

# Canviar la vida i la vida màxima
energies = [100, 50, 25]
var_globals.vida_jugador = energies[var_globals.dificultat]
var_globals.vida_max = var_globals.vida_jugador




var_globals.Clear() # fer una mica d'espai

#DEBUG: TEST IF DIFFICULTY SET CORRECTLY

#print("DEBUG: DIFICULTY:", var_globals.dificultat)

# Selecció de personatje (Limitat a uns en concret)
personatges = ["E", "ඞ", "8", "༏", "i", "ï"]
selecting = True
while selecting:
    var_globals.Clear()
    print(r'''


 _______  _______  _        _______  _______  _______ _________ _______  _        _______    
(  ____ \(  ____ \( \      (  ____ \(  ____ \(  ____ \\__   __/(  ___  )( (    /|(  ___  )   
| (    \/| (    \/| (      | (    \/| (    \/| (    \/   ) (   | (   ) ||  \  ( || (   ) |   
| (_____ | (__    | |      | (__    | |      | |         | |   | |   | ||   \ | || (___) |   
(_____  )|  __)   | |      |  __)   | |      | |         | |   | |   | || (\ \) ||  ___  |   
      ) || (      | |      | (      | |      | |         | |   | |   | || | \   || (   ) |   
/\____) || (____/\| (____/\| (____/\| (____/\| (____/\___) (___| (___) || )  \  || )   ( |   
\_______)(_______/(_______/(_______/(_______/(_______/\_______/(_______)|/    )_)|/     \|   
 _______  _______  _______  _______  _______  _        _______ _________ _______  _______  _ 
(  ____ )(  ____ \(  ____ )(  ____ \(  ___  )( (    /|(  ___  )\__   __/(  ____ \(  ____ \( )
| (    )|| (    \/| (    )|| (    \/| (   ) ||  \  ( || (   ) |   ) (   | (    \/| (    \/| |
| (____)|| (__    | (____)|| (_____ | |   | ||   \ | || (___) |   | |   | |      | (__    | |
|  _____)|  __)   |     __)(_____  )| |   | || (\ \) ||  ___  |   | |   | | ____ |  __)   | |
| (      | (      | (\ (         ) || |   | || | \   || (   ) |   | |   | | \_  )| (      (_)
| )      | (____/\| ) \ \__/\____) || (___) || )  \  || )   ( |   | |   | (___) || (____/\ _ 
|/       (_______/|/   \__/\_______)(_______)|/    )_)|/     \|   )_(   (_______)(_______/(_)
''')
    
    #Enumera els personatges
    for v, i in enumerate(personatges):
        print(f"{v+1}. {i}")
    user = input("Selecciona el teu personatge:")
    try:
        user = int(user)
        user = user-1
        if user < 0: continue
        var_globals.character_jugador = personatges[user]
        selecting = False
    except IndexError: # Si l'usuari no entra un numero
        pass
    except ValueError: # Si l'usuari no entra un numero dins del rang
        pass
    
del selecting
var_globals.Clear()

import mapa, moviments # La resta les importem aquí, així algunes configuracions no es desincronitzen (No llegeixin la dificultat abans de seleccionar-la)


map = mapa.GenerarMapa()
FOW = mapa.GenerarFOW(character="▬") # Prepara la Fog Of War, que no permet veure zones no visitades. Actuarà com a màscara quan es renderitzi el mapa



#print("DEBUG: MAP DIMENSIONS\n", mapa.x, mapa.y)

playing = True # Serà False quan la partida termini.
win = False # Serà True quan tots els animals siguin fotografiats

fow_distances = [2, 1.5, 1] # Les distàncies, per dificultat, que desvelarà el FOW
fow_radius = fow_distances[var_globals.dificultat]

moviments.UpdateFOW(FOW, fow_radius)
while playing:
    print(f"{var_globals.vida_jugador}/{var_globals.vida_max} ♥ ------ Sitting on: {map[var_globals.pos_jugador[1]][var_globals.pos_jugador[0]]}. Coords: {var_globals.pos_jugador}")
    print(mapa.RenderitzarMapa(map, FOW))
    print(f"Queden {var_globals.animals_restants} animals per fotografiar")
    moviments.moure(input("Selecciona el teu moviment:"), map)
    moviments.UpdateFOW(FOW, fow_radius) # Després de moure, actualitzar la FOW


    # Comprovar les condicions de victòria/derrota
    if var_globals.animals_restants == 0:
        playing = False
        win = True
    if var_globals.vida_jugador <= 0:
        playing = False


    var_globals.Clear() # Donar espai pq la terminal quedi neta


# Fin del joc, mostrar si el jugador ha guanyat o perdut
if win:
    print(r'''
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_'.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  &                    ~-~-~-~-~-~-~-~-~-~   /|
 ejm97    )      ~-~-~-~-~-~-~-~  /|~       /_|\
        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~
~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~
FELICITATS!
    Has fotografiat tots els animals de la zona!
          Gràcies per jugar.''')
else:
    print(r'''
                       _..gggggppppp.._                       
                  _.gd$$$$$$$$$$$$$$$$$$bp._                  
               .g$$$$$$P^^""j$$b""""^^T$$$$$$p.               
            .g$$$P^T$$b    d$P T;       ""^^T$$$p.            
          .d$$P^"  :$; `  :$;                "^T$$b.          
        .d$$P'      T$b.   T$b                  `T$$b.        
       d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b       
      d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b      
     d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b     
    d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P            T$$b    
   d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b   
  :$$$      .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.g.     $$$;  
  $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$  
 :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$; 
 $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$ 
:$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
:$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
$$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
$$$;      $$$$$$$$$$$$$$$                        Tb    _  :$$$
:$$$     d$$$$$$$$$$$$$$$.                        $b.__Tb $$$;
:$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
 $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$ 
 :$$$       T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$; 
  $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$  
  :$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;     $$$;  
   T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P   
    T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P    
     T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P     
      T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P      
       T$$b.      '       $$$$$$$$$$$$$$$$$$$$$$$$$$$$P       
        `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'        
          `T$$$$p..__..g$$$$$$$$$$$$$$$$$$$$$$$$$$P'          
            "^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^"            
               "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"               
                   """^^^T$$$$$$$$$$P^^^"""
Has perdut!
    Tinguis mes compte quan vagis de safari!''')



