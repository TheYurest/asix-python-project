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
print("\n"*25)
intro = '''

======BENVINGUTS AL PROJECTE======

BB   EEE  SSS TTTTT III  AA   L
B B  E   S      T    I  A  A  L
BB   EE   SS    T    I  AAAA  L
B B  E      S   T    I  A  A  L
BB   EEE SSS    T   III A  A  LLLL

'''


var_globals.RenderText("Selecciona la teva dificultat:\n1. Fàcil\n2. Normal\n3. Difícil", upperText=intro, delay=0.1)

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




var_globals.Clear() # fer una mica d'espai

#DEBUG: TEST IF DIFFICULTY SET CORRECTLY

#print("DEBUG: DIFICULTY:", var_globals.dificultat)


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



