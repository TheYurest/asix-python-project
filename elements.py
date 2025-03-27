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
    # Leaves: Si la casella ha de ser substituida per l'element per defecte

    def __init__(self, l, e=0, p=True, a=None, leaves=True):
        self.lletra = l[0] # Agafem la primera lletra, per si de cas intentem passar una string de més d'un caràcter
        self.energia = e
        self.passable = p
        self.accio = a
        self.leaves = leaves

    
    # Quan es vulgui fer servir com a string, retorna la lletra. Útil per representar el mapa
    def __str__(self):
        return self.lletra


class Vacuum(Element):  # Casella vuida, es pot passar, no té cap acció i no afecta en l'energia


    def __init__(self):
        Element.__init__(self, ".") # "/" per debug, però serà un espai vuit en la versió final




# Classe Animal (Herència: Element) - Retorna +5 d'energía en fàcil i mitg, +2 en difícil, es pot passar, i es representa amb la lletra "A"
import var_globals

class Animal(Element):


    def __init__(self, energia=[5,5,2][dificultat]):

        def accio(): 
            import var_globals
            var_globals.animals_restants -= 1
            #TO DO: ADD CINEMATIC OR SMTHN

        Element.__init__(self, "A",e=energia, a=accio) # si la dificultat és difícil, només +2 d'energia. Si no, +5


class Cacador(Element):    
  

    def __init__(self, energia=[-30, -40, -50][dificultat]):
        super().__init__("♔", energia)  # Associar acció al caçador




class Trampa(Element):

    def __init__(self, energia=[-20, -25, -30][dificultat]):
        Element.__init__(self, "T", energia, leaves=False)



class Llac(Element):
    def __init__(self, energia=[5,4,3][dificultat]):

        super().__init__("L", energia, leaves=True)  # L'acció del Llac s'executarà quan el jugador passi per sobre



class BoscDens(Element):  # Element que no es pot travessar
    def __init__(self, energia=0):
        Element.__init__(self, "B", 0, p=False)  # No es pot passar
   




default_element = Vacuum
