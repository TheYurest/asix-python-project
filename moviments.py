# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()
import var_globals # pos_jugador = [x, y]
#CODI AQUÍ


# Funció per moure el jugador segons la direcció d'entrada
def moure(dir):
    # Obtenir la posició actual del jugador
    x, y = var_globals.pos_jugador
    

#CODI: UNA FUNCIÓ QUE MOU EL JUGADOR DEPENEN DE LA INPUT (W: ADALT, S: ABALL...)
 # Calcular la nova posició segons la direcció
    if dir == 'W':  # Moure cap amunt
        new_y = (y - 1) % mapa.py  # Envoltar verticalment
        if mapa.mapa[new_y][x].passable:  # Comprovar si la nova posició és transitable
            var_globals.pos_jugador[1] = new_y  # Actualitzar la posició Y del jugador
    elif dir == 'S':  # Moure cap avall
        new_y = (y + 1) % mapa.py  # Envoltar verticalment
        if mapa.mapa[new_y][x].passable:  # Comprovar si la nova posició és transitable
            var_globals.pos_jugador[1] = new_y  # Actualitzar la posició Y del jugador
    elif dir == 'A':  # Moure cap a l'esquerra
        new_x = (x - 1) % mapa.x  # Envoltar horitzontalment
        if mapa.mapa[y][new_x].passable:  # Comprovar si la nova posició és transitable
            var_globals.pos_jugador[0] = new_x  # Actualitzar la posició X del jugador
    elif dir == 'D':  # Moure cap a la dreta
        new_x = (x + 1) % mapa.x  # Envoltar horitzontalment
        if mapa.mapa[y][new_x].passable:  # Comprovar si la nova posició és transitable
            var_globals.pos_jugador[0] = new_x  # Actualitzar la posició X del jugador
   
    # Actualitzar la Boira de Guerra o qualsevol altre estat del joc necessari
    UpdateFOW()

def UpdateFOW():
    # Aquesta funció es pot implementar per actualitzar la visibilitat del mapa
    # segons la posició actual del jugador. De moment, pot ser un marcador de posició.
    pass         

#HA D'ACTUALITZAR LA POSICIÓ DEL JUGADOR A var_globals.pos_jugador SEGONS LA INPUT. SI SURT DEL MAPA, HA DE TORNAR PER L'ALTRE COSTAT
