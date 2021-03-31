#TP : Nombres rationnels
Un nombre rationnel est un nombre qui peut s’écrire comme une fraction de deux entiers : numérateur 
et dénominateur (le dénominateur devant être non nul).

Ce TP a pour but de créer un programme qui va gérer des nombres rationnels, ce qui va amener à 
définir une classe qui créé le type Ratio, représentant un nombre rationnel.
Les instances de cette classe auront deux attributs : un numérateur et un dénominateur.
Cette classe devra être correctement encapsulée, munie d’accesseurs et de mutateurs pour chacun de 
ses attributs, et être robuste (ce qui signifie qu’elle doit être capable de générer des exceptions 
appropriées).

Elle sera notamment munie d’une méthode __str__ qui permet d’afficher ses instances sous la 
forme : n/d (n étant le numérateur et d le dénominateur).
Le programme principal demandera à l’utilisateur de saisir deux nombres rationnels (pour chacun 
d’entre eux : saisie d’un numérateur et d’un dénominateur corrects), puis affichera :
- les deux nombres rationnels saisis
- le résultat de leur addition, calculée à partir d’une instruction du type : r1 + r2
- le résultat de la division du premier nombre rationnel par le second (lorsque cette division est 
possible), calculée à partir d’une instruction du type : r1 / r2

La classe Ratio devra donc gérer la surcharge des opérateurs d’addition et de division.
De plus, on voudra que les résultats de ces deux opérations soient exprimés sous la forme de fractions 
simplifiées (on pourra pour cela utiliser la fonction gcd – à importer depuis le module math - qui 
permet de calculer le PGCD de deux entiers).

On voudra de plus que les dénominateurs des fractions exprimant ces résultats ne soient pas négatifs.
Enfin, si ces résultats sont entiers, on voudra qu’ils soient affichés comme des entiers
(Voir exemples d’exécution en page suivante).

Rappels mathématiques :

??/?? + ??/?? = (???? + ????) / ???? (avec ?? et ?? non nuls)
??/?? ÷ ??/?? = ???? / ???? (avec ??, ?? et ?? non nuls)
??/?? = (?? ÷ PGCD(??, ??)) / (?? ÷ PGCD(??, ??)) (avec ?? non nul)
??/??? = ??? / ?? (avec ?? non nul)
?? / 1 = ??

Exemple 1 :
Saisissez un premier nombre rationnel :
 Numérateur : 2b
 Dénominateur : 3
 Vous devez saisir des nombres entiers.
 Numérateur : 2
 Dénominateur : 3.5
 Vous devez saisir des nombres entiers.
 Numérateur : 5
 Dénominateur : 0
 Un dénominateur ne peut pas être égal à zéro.
 Numérateur : 3
 Dénominateur : -2
Saisissez un deuxième nombre rationnel :
 Numérateur : -5
 Dénominateur : 2
Le premier nombre rationnel saisi est : 3/-2
Le deuxième nombre rationnel saisi est : -5/2
Résultat de l'addition des deux nombres rationnels saisis : -4
Résultat de la division du premier nombre rationnel saisi par le deuxième : 3/5
Exemple 2 :
Saisissez un premier nombre rationnel :
 Numérateur : 15
 Dénominateur : -9
Saisissez un deuxième nombre rationnel :
 Numérateur : 0
 Dénominateur : 7
Le premier nombre rationnel saisi est : 15/-9
Le deuxième nombre rationnel saisi est : 0/7
Résultat de l'addition des deux nombres rationnels saisis : -5/3
Résultat de la division du premier nombre rationnel saisi par le deuxième :
Division impossible car le deuxième nombre rationnel est nul