# elements.py: Defineix els elements i les seves característiques.

if __name__=="__main__":
    print("ERROR: s'ha d'executar l'arxiu \"ppal.py\"")
    exit()


# Classe element. Farem servir herència per a cada element
class Element:

    # Lletra: La lletra per la que serà representada
    # Energia: La quantitat d'energia que afagirà al jugador (o treurà, si és negatiu)
    # Passable: Si el jugador pot passar per sobre d'aquesta casella (El bosc no es pot passar, pel que serà False.)

    def __init__(self, l, e=0, p=True):
        self.lletra = l[0] # Agafem la primera lletra, per si de cas intentem passar una string de més d'un caràcter
        self.energia = e
        self.passable = p
    
    # Quan es vulgui fer servir com a string, retorna la lletra. Útil per representar el mapa
    def __string__(self):
        return self.lletra

# Classe Animal (Herència: Element) - Retorna +5 d'energía, es pot passar, i es representa amb la lletra "A"
class Animal(Element):
    def __init__(self):
        Element.__init__("A", 5)