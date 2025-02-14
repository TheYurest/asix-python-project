# moviments.py: Implementa les regles per moure l’explorador.
if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()
import var_globals # pos_jugador = [x, y]
#CODI AQUÍ

#CODI: UNA FUNCIÓ QUE MOU EL JUGADOR DEPENEN DE LA INPUT (W: ADALT, S: ABALL...)
#HA D'ACTUALITZAR LA POSICIÓ DEL JUGADOR A var_globals.pos_jugador SEGONS LA INPUT. SI SURT DEL MAPA, HA DE TORNAR PER L'ALTRE COSTAT

#TAMBÉ HA D'ACTUALITZAR LA FOW (una funció UpdateFOW que agafi la FOW actual, i retornarà una nova per on es pugui veure el jugador)
#LA FOW TÉ AQUEST FORMAT: "#" a les caselles que no es poden veure, i 0 a les caselles que si que es poden veure

def moure(dir):
    pass # CODI AQUI, CAL TREURE "pass"

def UpdateFOW(fow):
    pass # CODI AQUI, CAL TREURE "pass"