# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()
from var_globals import pos_jugador # pos_jugador = [x, y]
# Ara es pot fer referència a "pos_jugador" directament, sense escriure "var_globals.pos_jugador"










# Funció per moure el jugador segons la direcció d'entrada i el mapa actual
# El mapa és una matriu, en la que els elements tenen una propietat "passable" i una "energia". Si "passable" és True, el jugador pot moure's allà, i llavors s'aplicarà la suma/resta d'energia.
def moure(dir, mapa):
    # Obtenir la posició actual del jugador
    x, y = pos_jugador
    

    # Aquesta part mou el jugador adalt si la direcció és "W". Cuando funcione entonces puedes hacer lo mismo con ASD.
    if dir == 'W':
        new_y = (y - 1) % mapa.py
        if mapa.mapa[new_y][x].passable:
            pos_jugador[1] = new_y
   
    # Actualitzar la Boira de Guerra o qualsevol altre estat del joc necessari
    UpdateFOW()











def UpdateFOW():
    # Aquesta funció es pot implementar per actualitzar la visibilitat del mapa
    # segons la posició actual del jugador.
    pass         

#HA D'ACTUALITZAR LA POSICIÓ DEL JUGADOR A var_globals.pos_jugador SEGONS LA INPUT. SI SURT DEL MAPA, HA DE TORNAR PER L'ALTRE COSTAT
