from Ratio import Ratio
def main():
    print("Saisissez un premier nombre rationnel:")
    numerateur = input("Numérateur : ")
    denominateur = input("Dénominateur : ")
    try:
        Ratio(numerateur,denominateur)
    except ValueError:
        print("Veuillez entrer un nombre positif")
    except Exception as e:
        print(type(e))
        print(e)

main()