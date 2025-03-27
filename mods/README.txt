Aquesta carpeta contindrà els mods.
La documentació per poder fer els teus propis mods estarà disponible a la pàgina de GitHub, però aquest serà el format amb el que començarem:

Cada mod serà una carpeta que contindrà aquests arxius:
modinfo.json
defaults.json
elems.json
difs.json

Tots els arxius son obligatoris, però "elems.json" pot estar vuit


 _____ ____ _____ ____  _   _  ____ _____ _   _ ____  _____ ____  
| ____/ ___|_   _|  _ \| | | |/ ___|_   _| | | |  _ \| ____/ ___| 
|  _| \___ \ | | | |_) | | | | |     | | | | | | |_) |  _| \___ \ 
| |___ ___) || | |  _ <| |_| | |___  | | | |_| |  _ <| |___ ___) |
|_____|____/ |_| |_| \_\\___/ \____| |_|  \___/|_| \_\_____|____/ 

Nota: totes les variables obligatories estàn prefixades amb "*", així "*name" és una variable obligatoria que es diu "name"


modinfo.json:
- *name: tipus string, conté el nom del mod
- *description: tipus string, conté la descripció del mod
- author: tipus string, conté l'autor del mod
- version: tipus string, si no s'especifica serà "1.0.0" per defecte
- banner: tipus string, el text que es mostrarà quan el jugador accedeixi al mod. string vuida per defecte



defaults.json:
Aquest arxiu ha de tenir una array per a cada element ja programat (Animal, Llac, Rei [Caçador], Bosc i Trampa).
Les arrays contindran les energies dels elements a les dificultats extres afegides a difs.json





elems.json
- *name: Nom de l'element
- *char: String, lletra que representarà a l'element al mapa. Si es passa una string llarga, només s'acceptarà el primer caràcter
- energies: Array de ints. Representarà les energies que l'element donarà (positiu) o treurà (negatiu) al jugador en passar per sobre. Si no s'especifica, serà sempre 0
	Format: Els tres primers ints han de ser per les dificultats ja programades (Fàcil, normal i difícil), i després una per cada dificultat extra a difs.json
