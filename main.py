from Ratio import Ratio
def fraction (numerateur, denominateur):
    try:
        return Ratio(numerateur, denominateur)
    except ValueError:
        print("Vous devez saisir des nombres entiers.")
    except Exception as e:
        print(type(e))
        print(e)

def main():
    #Demande ma première fraction
    print("Saisissez un premier nombre rationnel :")
    numerateur1 = input("Numérateur : ")
    denominateur1 = input("Dénominateur : ")

    r1 = fraction(numerateur1, denominateur1)

    #Demande ma deuxième fractions
    print("Saisissez un deuxième nombre rationnel :")
    numerateur2 = input("Numérateur : ")
    denominateur2 = input("Dénominateur : ")

    try:
        r2 = Ratio(numerateur2,denominateur2)
    except ValueError:
        print("Vous devez saisir des nombres entiers.")
        main()

main()