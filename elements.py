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

    def __init__(self, l, e=0, p=True, a=None, leaves=False):
        self.lletra = l[0] # Agafem la primera lletra, per si de cas intentem passar una string de més d'un caràcter
        self.energia = e
        self.passable = p
        self.accio = a
        self.leaves = leaves

    
    # Quan es vulgui fer servir com a string, retorna la lletra. Útil per representar el mapa
    def __str__(self):
        return self.lletra



class Vacuum(Element): # Casella vuida, es pot passar, no té cap acció i no afecta en l'energia

    def __init__(self):
        Element.__init__(self, ".") # "/" per debug, però serà un espai vuit en la versió final




# Classe Animal (Herència: Element) - Retorna +5 d'energía en fàcil i mitg, +2 en difícil, es pot passar, i es representa amb la lletra "A"
class Animal(Element):


    def __init__(self):

        def accio():
            
            import var_globals
            var_globals.animals_restants -= 1
            var_globals.Clear()

            animals = [r'''
       _------.
      /  ,     \_
    /   /  /{}\ |o\_
   /    \  `--' /-' \
  |      \      \    |
 |              |`-, |
 /              /__/)/
|              |

Has fotografiat un lloro!''', r'''
                              ___,--------,____
                      __--~~~~                 ~~---,_
                   ,-'                  __,--,_       `\,___,-,__
                ,-'                 __/'/-~~~\  `  ` . '    , |  `~~\
             _/`      _/~~      '~~   \,_\_ O /        '  '~_/'      `\
           /'        '                   =-'~~  _  /  ~   /'          `\
        _/'  /~                            ,--,____,-----|,_,-,_       `\
    _,/'    '              ,-'      _      `~'------'~~~~~--    `~~~~\  |
 ,-'             /~       '    ,-~~~         _,       ,-=~~~~~~~~~~~~'| |
~              .'             '         ,   '      /~`                |/
                                  /' ,/'       _/~'
                   ,       /    /`          _/~ 
        /~        /      /`               /' 
      .'                                /' 
                       /'      .      /
                      `       /'     | 
                                    '
Has fotografiat una àguila! Impresionant!''', r'''
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
            __//--'/`   hjw
          ,--'/`  '
             '

Has fotografiat una gallina!''', r'''

            _.-.
        .-.  `) |  .-. 
    _.'`. .~./  \.~. .`'._
.-'`.'-'.'.-:    ;-.'.'-'.`'-.
 `'`'`'`'`   \  /   `'`'`'`'`
             /||\
            / ^^ \
            `'``'`
Has fotografiat un ocell!''', r'''
                                  z-                                         
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
                                  """"""""
Com?! Has fotografiat la Draca de Solsona!
Feliç Carnaval!''',r'''
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
Atrapal's a tots!''',r'''
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
Espera, és rosa?''']
            
            

            from random import randint as r
            input(animals[r(0, len(animals)-1)])

        Element.__init__(self, "A", e=2 if dificultat==2 else 5, a=accio, leaves=True) # si la dificultat és difícil, només +2 d'energia. Si no, +5


class Cacador(Element):

    def __init__(self):

        def accio():
            from var_globals import Clear
            Clear()

            input(r'''
           ___      |\________/)
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
           |    /

El rei t'ha confòs per un animal i t'ha disparat!
''')


        energies = [-30, -40, -50]
        Element.__init__(self, "C", e=energies[dificultat], leaves=True, a=accio)



class Trampa(Element):



    def __init__(self):

        def accio():
            from var_globals import Clear
            Clear()
            input(r'''
            ________
            \       \
  ________   \____   \
  \       \      /   /
   \____   \____/   /   ____
       /            \   \   \
  ____/   ________   \   \   \
 /        \       \   \  /
/   ____   \____   \   \/
\   \   \      /   /
 \   \   \____/   /   ____
  \  /            \  /   /
   \/   ________   \/   /
        \       \      /
         \____   \____/
             /
        ____/
Has caigut en una trampa!''')

        energies = [-20, -25, -30]
        Element.__init__(self, "T", e=energies[dificultat], leaves=False, a=accio)

class Llac(Element):
    

    
    
    from var_globals import dificultat
    def __init__(self):
            energies = [5, 5, 2]
            def accio():

              input('''
     ,%&& %&& %
   ,%&%& %&%& %&
  %& %&% &%&% % &%
 % &%% %&% &% %&%&,
 &%&% %&%& %& &%& %
%%& %&%& %&%&% %&%%&
&%&% %&% % %& &% %%&
&& %&% %&%& %&% %&%'
 '%&% %&% %&&%&%%'%
  % %& %& %&% &%%
    `\%%.'  /`%&'
      |    |            /`-._           _\\/
      |,   |_          /     `-._ ..--~`_
      |;   |_`\_      /  ,\\.~`  `-._ -  ^
      |;:  |/^}__..-,@   .~`    ~    `o ~
      |;:  |(____.-'     '.   ~   -    `    ~
      |;:  |  \ / `\       //.  -    ^   ~
      |;:  |\ /' /\_\_        ~. _ ~   -   //-
 jgs\\/;:   \'--' `---`           `\\//-\\///
T'has trobat un llac!
  Has recuperat vida.''')
            Element.__init__(self, "L", e=energies[dificultat], p=True, a=accio, leaves=True)



class Refugi(Element):
    def __init__(self):
        
        def accio():
            from var_globals import Clear
            Clear()

            input(r'''
                  .e$c"*eee...         
                z$$$$$$.  "*$$$$$$$$$.                    
            .z$$$$$$$$$$$e. "$$$$$$$$$$c.                 
         .e$$P""  $$  ""*$$$bc."$$$$$$$$$$$e.             
     .e$*""       $$         "**be$$$***$   3             
     $            $F              $    4$r  'F            
     $           4$F              $    4$F   $            
    4P   \       4$F              $     $$   3r           
    $"    r      4$F              3     $$r   $           
    $     '.     $$F              4F    4$$   'b          
   dF      3     $$    ^           b     $$L   "L         
   $        .    $$   %            $     ^$$r   "c        
  JF             $$  %             4r     '$$.   3L       
 .$              $$ "               $      ^$$r""         
 $%              $$P                3r  .e*"              
'*=*********************************$$P"
    T'has trobat un refugi!
        Has recuperat tota l'energia!''')

        Element.__init__(self , l="⌂", e=9999, a=accio, leaves=True)


class Bosc(Element):
    

    def __init__(self):
        def accio():
            from var_globals import Clear
            Clear()
            input(r'''
      /\      /\      /\      /\      /\      /\      /\      /\
     /**\    /**\    /**\    /**\    /**\    /**\    /**\    /**\
    /****\  /****\  /****\  /****\  /****\  /****\  /****\  /****\
   /      \/      \/      \/      \/      \/      \/      \/      \
  /  /\    \ /\    \ /\    \ /\    \ /\    \ /\    \ /\    \ /\
 /  /**\    /**\    /**\    /**\    /**\    /**\    /**\    /**\    /**\
/____**\__/****\__/****\__/****\__/****\__/****\__/****\__/****\__/****\__
     ||       ||       ||       ||       ||       ||       ||       ||
     ||       ||       ||       ||       ||       ||       ||       ||
     ||       ||       ||       ||       ||       ||       ||       ||
No pots passar per aquí, el bosc és massa dens.
    Busca un altre camí, recorda que el mapa és esfèric.''')


        Element.__init__(self, "B", p=False, a=accio)

default_element = Vacuum