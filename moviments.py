# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()
from var_globals import pos_jugador # pos_jugador = [x, y]
# Ara es pot fer referència a "pos_jugador" directament, sense escriure "var_globals.pos_jugador"

# Funció per moure el jugador segons la direcció d'entrada i el mapa actual
# El mapa és una matriu, en la que els elements tenen una propietat "passable" i una "energia". Si "passable" és True, el jugador pot moure's allà, i llavors s'aplicarà la suma/resta d'energia.
def moure(dir, mapa):    
    from var_globals import vida_jugador

    # Obtenir la posició actual del jugador
    x, y = pos_jugador
    dir = dir.upper()

    # Aquesta part mou el jugador adalt si la direcció és "W". Si el jugador intenta moure's a un Bosc dens, no es permetrà el moviment.
    if dir == 'W' and mapa[y-1][x].passable:
        pos_jugador [1] -= 1
        if pos_jugador [1] < 0:
            pos_jugador [1] = len(mapa) -1            
    elif dir == 'S' and mapa[y+1][x].passable:
        pos_jugador [1] += 1
        if pos_jugador [1] >= len(mapa):
            pos_jugador [1] = 0
    elif dir == 'A' and mapa[y][x-1].passable:
        pos_jugador [0] -= 1
        if pos_jugador [0] < 0:
            pos_jugador [0] = len(mapa[0]) -1
    elif dir == 'D' and mapa[y][x+1].passable:
        pos_jugador [0] += 1
        if pos_jugador[0] >= len(mapa[0]):
            pos_jugador[0] = 0 
    
    x,y=pos_jugador
    if mapa[y][x].accio != None:        
        mapa[y][x].accio()  # Call the action method to modify vida_jugador 
        
    import var_globals
    var_globals.vida_jugador = min(vida_jugador+mapa[y][x].energia, var_globals.vida_max[var_globals.dificultat])

    from elements import default_element
    if mapa[y][x].leaves:
        mapa[y][x] = default_element()
    


def UpdateFOW(fow, r=2):
    from math import dist
    from var_globals import pos_jugador
    px, py = pos_jugador
    for fy in range(len(fow)):
        for fx in range(len(fow[0])):
            if dist([fx,fy], [px, py]) <= r: fow[fy][fx] = 0

#HA D'ACTUALITZAR LA POSICIÓ DEL JUGADOR A var_globals.pos_jugador SEGONS LA INPUT. SI SURT DEL MAPA, HA DE TORNAR PER L'ALTRE COSTAT
