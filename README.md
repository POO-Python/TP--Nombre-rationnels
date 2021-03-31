#TP : Nombres rationnels
Un nombre rationnel est un nombre qui peut s��crire comme une fraction de deux entiers : num�rateur 
et d�nominateur (le d�nominateur devant �tre non nul).

Ce TP a pour but de cr�er un programme qui va g�rer des nombres rationnels, ce qui va amener � 
d�finir une classe qui cr�� le type Ratio, repr�sentant un nombre rationnel.
Les instances de cette classe auront deux attributs : un num�rateur et un d�nominateur.
Cette classe devra �tre correctement encapsul�e, munie d�accesseurs et de mutateurs pour chacun de 
ses attributs, et �tre robuste (ce qui signifie qu�elle doit �tre capable de g�n�rer des exceptions 
appropri�es).

Elle sera notamment munie d�une m�thode __str__ qui permet d�afficher ses instances sous la 
forme : n/d (n �tant le num�rateur et d le d�nominateur).
Le programme principal demandera � l�utilisateur de saisir deux nombres rationnels (pour chacun 
d�entre eux : saisie d�un num�rateur et d�un d�nominateur corrects), puis affichera :
- les deux nombres rationnels saisis
- le r�sultat de leur addition, calcul�e � partir d�une instruction du type : r1 + r2
- le r�sultat de la division du premier nombre rationnel par le second (lorsque cette division est 
possible), calcul�e � partir d�une instruction du type : r1 / r2

La classe Ratio devra donc g�rer la surcharge des op�rateurs d�addition et de division.
De plus, on voudra que les r�sultats de ces deux op�rations soient exprim�s sous la forme de fractions 
simplifi�es (on pourra pour cela utiliser la fonction gcd � � importer depuis le module math - qui 
permet de calculer le PGCD de deux entiers).

On voudra de plus que les d�nominateurs des fractions exprimant ces r�sultats ne soient pas n�gatifs.
Enfin, si ces r�sultats sont entiers, on voudra qu�ils soient affich�s comme des entiers
(Voir exemples d�ex�cution en page suivante).

Rappels math�matiques :

??/?? + ??/?? = (???? + ????) / ???? (avec ?? et ?? non nuls)
??/?? � ??/?? = ???? / ???? (avec ??, ?? et ?? non nuls)
??/?? = (?? � PGCD(??, ??)) / (?? � PGCD(??, ??)) (avec ?? non nul)
??/??? = ??? / ?? (avec ?? non nul)
?? / 1 = ??

Exemple 1 :
Saisissez un premier nombre rationnel :
 Num�rateur : 2b
 D�nominateur : 3
 Vous devez saisir des nombres entiers.
 Num�rateur : 2
 D�nominateur : 3.5
 Vous devez saisir des nombres entiers.
 Num�rateur : 5
 D�nominateur : 0
 Un d�nominateur ne peut pas �tre �gal � z�ro.
 Num�rateur : 3
 D�nominateur : -2
Saisissez un deuxi�me nombre rationnel :
 Num�rateur : -5
 D�nominateur : 2
Le premier nombre rationnel saisi est : 3/-2
Le deuxi�me nombre rationnel saisi est : -5/2
R�sultat de l'addition des deux nombres rationnels saisis : -4
R�sultat de la division du premier nombre rationnel saisi par le deuxi�me : 3/5
Exemple 2 :
Saisissez un premier nombre rationnel :
 Num�rateur : 15
 D�nominateur : -9
Saisissez un deuxi�me nombre rationnel :
 Num�rateur : 0
 D�nominateur : 7
Le premier nombre rationnel saisi est : 15/-9
Le deuxi�me nombre rationnel saisi est : 0/7
R�sultat de l'addition des deux nombres rationnels saisis : -5/3
R�sultat de la division du premier nombre rationnel saisi par le deuxi�me :
Division impossible car le deuxi�me nombre rationnel est nul