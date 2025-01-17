# elements.py: Defineix els elements i les seves característiques.

if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()



from var_globals import dificultat # 0, 1 o 2 = Fàcil, Mitg o Difícil



# Classe element. Farem servir herència per a cada element
class Element:

    # Lletra: La lletra per la que serà representada
    # Energia: La quantitat d'energia que afagirà al jugador (o treurà, si és negatiu)
    # Passable: Si el jugador pot passar per sobre d'aquesta casella (El bosc no es pot passar, pel que serà False.)
    # Acció: La funció que s'executarà quan el jugador passi per l'element (Funcionalitat extra, per exemple, cinemàtica)


    def __init__(self, l, e=0, p=True, a=None):
        self.lletra = l[0] # Agafem la primera lletra, per si de cas intentem passar una string de més d'un caràcter
        self.energia = e
        self.passable = p
        self.accio = a

    
    # Quan es vulgui fer servir com a string, retorna la lletra. Útil per representar el mapa
    def __string__(self):
        return self.lletra








# Classe Animal (Herència: Element) - Retorna +5 d'energía en fàcil i mitg, +2 en difícil, es pot passar, i es representa amb la lletra "A"
class Animal(Element):



    def __init__(self):

        def accio():
            pass

        Element.__init__("A", 2 if dificultat==2 else 5, a=accio) # si la dificultat és difícil, només +2 d'energia. Si no, +5


class Cacador(Element):

    def __init__(self):
        Element.__init__("C", )