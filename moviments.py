# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()
# Ara es pot fer referència a "pos_jugador" directament, sense escriure "var_globals.pos_jugador"

# Funció per moure el jugador segons la direcció d'entrada i el mapa actual
# El mapa és una matriu, en la que els elements tenen una propietat "passable" i una "energia". Si "passable" és True, el jugador pot moure's allà, i llavors s'aplicarà la suma/resta d'energia.
def moure(dir, mapa):    
    from var_globals import vida_jugador, pos_jugador
    import var_globals

    # Obtenir la posició actual del jugador
    x, y = var_globals.pos_jugador
    dir = dir.upper()
    # Aquesta part mou el jugador adalt si la direcció és "W". Si el jugador intenta moure's a un Bosc dens, no es permetrà el moviment.
    direccions = {
        "W":[-1, 0],
        "A":[0, -1],
        "S":[1, 0],
        "D":[0, 1]
    }

    if dir in direccions:
        dir = direccions[dir]
    else:
        dir = [0,0]
    
    target = mapa[(y+dir[1])%len(mapa)][(x+dir[0])%len(mapa[0])]

    if target.accio != None:        
        target.accio()


    if target.passable:
        x, y = [x+dir[0],y+dir[1]]
        
    # comprova si el jugador ha sortit del mapa
    if x<0: x=len(mapa[0])-1
    if y<0: y=len(mapa)-1
    if x>=len(mapa[0]): x=0
    if y>=len(mapa): y=0
    
    var_globals.pos_jugador = [x,y]


    # # # # Implementació vella del moviment
    #
    # if dir == 'W' and mapa[y-1][x].passable:
    #     pos_jugador [1] -= 1
    #     if pos_jugador [1] < 0:
    #         pos_jugador [1] = len(mapa) -1            
    # elif dir == 'S' and mapa[y+1][x].passable:
    #     pos_jugador [1] += 1
    #     if pos_jugador [1] >= len(mapa):
    #         pos_jugador [1] = 0
    # elif dir == 'A' and mapa[y][x-1].passable:
    #     pos_jugador [0] -= 1
    #     if pos_jugador [0] < 0:
    #         pos_jugador [0] = len(mapa[0]) -1
    # elif dir == 'D' and mapa[y][x+1].passable:
    #     pos_jugador [0] += 1
    #     if pos_jugador[0] >= len(mapa[0]):
    #         pos_jugador[0] = 0
    
    x,y=var_globals.pos_jugador
    
    
    var_globals.vida_jugador = min(vida_jugador+mapa[y][x].energia, var_globals.vida_max)

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

