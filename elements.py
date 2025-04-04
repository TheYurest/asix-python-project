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
            #MOSTRA UNA FOTO D'UN ANIMAL RANDOM DE LA LLISTA
            imatges = [r"""       _                        
       \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
      .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'
        Has fotografiat un gat!""", r"""                                                         _...---.._
                                                     _.'`       -_  `.
                                                 .-'`                  \
                                              .-`                     q
                                           _-`                       __  \
                                       .-'`                  . ' .   \ `;/
                                   _.-`                    /       `._`/
                           _...--'`                        \_
                        .'`                         -         `'--.._
                     . `                           \                  `-.
                    .                `              `-..__. ... - -.._`-
                   '.                `  '''---- -''`                  `-.`.
                 .` -                '`.  `-.
              .-` .` '             .`'.__ ;
          _.-` .-`   '            .
      _.-`  .-`       '         .`
(`''-'' _.-`          '        .'
 `'---''            .`       .`
                 .'     . '`
                .    .-`
              .`   ,`
             '   .'
           '   .`
          '  .`
          `  '.
          `.___;
    Has fotografiat un puma!""", r"""              :     :
        __    |     |    _,_
       (  ~~^-l_____],.-~  /
        \    ")\ "^k. (_,-"
         `>._  ' _ `\  \
      _.-~/'^k. (0)  ` (0
   .-~   {    ~` ~    ..T
  /   .   "-..       _.-'
 /    Y        .   "T
Y     l         ~-./l_
|      \          . .<'
|       `-.._  __,/"r'
l   .-~~"-.    /    I
 Y         Y "~[    |
  \         \_.^--, [
   \            _~> |
    \      ___)--~  |
     ^.       :     l
       ^.   _.j     |
         Y    I     |
         l    l     I
          Y    \    |
           \    ^.  |
            \     ~-^.
             ^.       ~"--.,_
              |~-._          ~-.
              |    ~Y--.,_      ^.
              :     :     "x      \
                            \      \.
                             \      ]
                              ^._  .^
    Has fotografiat un esquirol volador!""", r"""                                  z-                                         
                                 d$                                          
                               .$$F                                          
                              z$$$                             d$$b     .$$  
-                            J$$$$                            d$. $$$$$$$$$  
  \                         4$$$$$                           z$$$$$$$$$$$$"  
   "c                       $$$$$$F                         d$$$*$$$$"       
    "$e.      .            $$$$$$$$                       .$$$$$             
     3$$$$$$P"             $$$$$$$$c                    .$$$$$$              
      $$$$$"               $$$$$$$$$r                .e$$$$$$$F              
      *$$$b                $$$$$$$$$$c           .e$$$$$$$$$$P               
      '$P "$.              $$$$$$$$$$$b.    .ee$$$$$$$$$$$$$P                
       $   ^$$.             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F                 
       "     $$$$e..      .e$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"                  
      4       "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P                    
                *$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P                      
                  "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*                        
                     "*$$$$$$$$$$$$$$$$$$$$$$$$$$$"                          
                         "*$$$$$$$$$$$$$$$$$$$$$"                            
                             *$$$$$$$$$$$$$$$"                               
                                  ''''''''
    Has fotografiat la draca de Solsona! Feliç Carnaval!""", r'''
  .--.            .--.
 ( (`\\."--``--".//`) )
  '-.   __   __    .-'
   /   /__\ /__\   \
  |    \ 0/ \ 0/    |
  \     `/   \`     /
   `-.  /-"""-\  .-`
     /  '.___.'  \
     \     I     /
      `;--'`'--;`
        '.___.'
Has fotografiat una pantera!
Espera, és rosa?''',r'''
       _------.
      /  ,     \_
    /   /  /{}\ |o\_
   /    \  `--' /-' \
  |      \      \    |
 |              |`-, |
 /              /__/)/
|              |

Has fotografiat un lloro!''',r'''
      ,~.
   ,-'__ `-,
  {,-'  `. }              ,')
 ,( a )   `-.__         ,',')~,
<=.) (         `-.__,==' ' ' '}
  (   )                      /
   `-'\   ,                  )
       |  \        `~.      /
       \   `._        \    /
        \     `._____,'   /
         `-.            ,'
            `-.      ,-'
               `~~~~'
               //_||
            __//--'/`
          ,--'/`  '
             '

Has fotografiat una gallina!''',r'''
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \
        :##.       ==             .###.       `.      `.    `\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:'

Com?! Has fotografiat un Pikachu!
Atrapal's a tots!''']
            from random import randint as r
            var_globals.Clear()
            print(imatges[r(0, len(imatges)-1)])
            input("\nPrem enter per continuar...")

        Element.__init__(self, "A",e=energia, a=accio) # si la dificultat és difícil, només +2 d'energia. Si no, +5


class Cacador(Element):    
  
    

    def __init__(self, energia=[-30, -40, -50][dificultat]):
        def accio():
            from var_globals import Clear
            Clear()
            print(r'''           ___      |\________/)
          [_,_])    \ /       \|
         /|=T=|]     /   __  __\
         |\ " //     |_  9   p ]\
         ||'-'/--.  / /\ =|  \|\ \
        /|| <\/> |\ | '._, @ @)<_)
       | |\   |  |   \.__/(_;_)
       |  .   H  |   |  :  '='|
       |  |  _H__/  _| :      |
        \  '.__  \ /  ;      ';
       __'-._(_}==.'  :       ;
      (___|    /-' |   :.     :
     [.-'  \   |   \   \ ;   :
    .-'     |  |    |  |   ":
   /        |==|     \  \  /  \_
  /         [  |      '._\_ -._ \
 /           \__)   __.- \ \   )\\
/       |        /.'      >>)
|        \       |\     |
|     .'  '-.    | \    /
|    /     /     / /   /
     snd   |    /
    El rei t'ha confòs per un animal i t'ha disparat!
        *Aquest rei ha fugit del tauler...''')
            input("\nPrem enter per continuar...")
        super().__init__("♔", energia, a=accio)  # Associar acció al caçador




class Trampa(Element):

    def __init__(self, energia=[-20, -25, -30][dificultat]):
        Element.__init__(self, "T", energia, leaves=False)



class Llac(Element):
    def __init__(self, energia=[5,4,3][dificultat]):

        super().__init__("L", energia, leaves=True)  # L'acció del Llac s'executarà quan el jugador passi per sobre



class BoscDens(Element):  # Element que no es pot travessar
    def __init__(self, energia=0):
        
        def accio():
            from var_globals import Clear
            Clear()
            print(r'''
      /\      /\      /\      /\      /\      /\      /\      /\
     /**\    /**\    /**\    /**\    /**\    /**\    /**\    /**\
    /****\  /****\  /****\  /****\  /****\  /****\  /****\  /****\
   /      \/      \/      \/      \/      \/      \/      \/      \
  /  /\     /\      /\      /\      /\      /\      /\      /\     \/\
 /  /**\   /**\    /**\    /**\    /**\    /**\    /**\    /**\    /**\
/__/****\_/****\__/****\__/****\__/****\__/****\__/****\__/****\__/****\
     ||       ||       ||       ||       ||       ||       ||       ||
     ||       ||       ||       ||       ||       ||       ||       ||
     ||       ||       ||       ||       ||       ||       ||       ||
No pots passar per aquí, el bosc és massa dens.
    Busca un altre camí, recorda que el mapa és esfèric.''')
            input("\nPrem enter per continuar")

        Element.__init__(self, "B", 0, p=False, a=accio)  # No es pot passar

class Refugi(Element): #Recuperar tota l'energia
    def __init__(self):
        from var_globals import vida_max
        super().__init__("R", vida_max, leaves=False)  # Recupera tota l'energia del jugador




default_element = Vacuum
