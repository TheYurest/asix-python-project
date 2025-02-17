# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()


# Funció per moure el jugador segons la direcció d'entrada i el mapa actual
# El mapa és una matriu, en la que els elements tenen una propietat "passable" i una "energia". Si "passable" és True, el jugador pot moure's allà, i llavors s'aplicarà la suma/resta d'energia.
def moure(dir, mapa):
    from var_globals import pos_jugador
    from elements import default_element

    # Obtenir la posició actual del jugador
    x, y = pos_jugador
    dir = dir.lower()
    map_x = len(mapa[0])
    map_y = len(mapa)

    # Aquesta part prepara les noves coordenades i les comprova
    if dir == 'w':
        y-=1
    elif dir == 's':
        y+=1
    elif dir == 'a':
        x-=1
    elif dir == 'd':
        x+=1
    x, y, = x%map_x, y%map_y
    
    import var_globals
    var_globals.vida_jugador = min(var_globals.vida_max, var_globals.vida_jugador+mapa[y][x].energia)
    



    # Finalment, si la casella és disponible, moure el jugador
    if mapa[y][x].passable:
        pos_jugador[0], pos_jugador[1] = x, y

    if mapa[y][x].accio != None: mapa[y][x].accio()

    if mapa[y][x].leaves: mapa[y][x] = default_element()
        
    
    


    # Actualitzar la Boira de Guerra o qualsevol altre estat del joc necessari
    UpdateFOW()











def UpdateFOW():
    # Aquesta funció es pot implementar per actualitzar la visibilitat del mapa
    # segons la posició actual del jugador.
    pass         

#HA D'ACTUALITZAR LA POSICIÓ DEL JUGADOR A var_globals.pos_jugador SEGONS LA INPUT. SI SURT DEL MAPA, HA DE TORNAR PER L'ALTRE COSTAT
