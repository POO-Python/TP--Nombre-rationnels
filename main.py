from Ratio import Ratio


#Initialisation des variables
r1 = None
r2 = None

numerateur1 = None
denominateur1 = None

numerateur2 = None
denominateur2 = None

#Fonction qui permet de saisir la première fraction
#Renvoie une instance de la Classe Ratio

def saisie_1er_fraction():
    #Demande ma première fraction
    print("\nSaisissez un premier nombre rationnel :")
    numerateur1 = input("Numérateur : ")
    denominateur1 = input("Dénominateur : ")
    try:
         return Ratio(int(numerateur1), int(denominateur1))

    except ValueError:
        print("Vous devez saisir des nombres entiers.\n")
        saisie_1er_fraction()
    except ZeroDivisionError:
        print("Un dénominateur ne peut pas être égal à zéro.\n")
        saisie_1er_fraction()
    except Exception as e:
        print("Une erreur est survenue")

#Fonction qui permet de saisir la deuxième fractions
#Renvoie une instance de la Classe Ratio

def saisie_2eme_fractions():
    #Demande ma deuxième fractions
    print("\nSaisissez un deuxième nombre rationnel :")
    numerateur2 = input("Numérateur : ")
    denominateur2 = input("Dénominateur : ")

    try:
        return Ratio(int(numerateur2),int(denominateur2))
    except ValueError:
        print("Vous devez saisir des nombres entiers.\n")
        saisie_2eme_fractions()
    except ZeroDivisionError:
        print("Un dénominateur ne peut pas être égal à zéro.\n")
        saisie_2eme_fractions()
    except Exception as e:
        print("Une erreur est survenue")


#Fonction Principal
def main():
    
    r1 = saisie_1er_fraction()
    print("\nLe premier nombre rationnel saisi est : ", r1)

    r2 = saisie_2eme_fractions()
    print("\nLe deuxième nombre rationnel saisi est : ", r2)

    print(r1 + r2)

    try:
        print(r1 / r2)
    except ZeroDivisionError:
        print("Division impossible car le deuxième nombre rationnel est nul.")


main()