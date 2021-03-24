from Ratio import Ratio
def main():

    try:
        Ratio('azerty',2,3,4)
    except ValueError:
        print("Veuillez entrer un nombre positif")
    except Exception as e:
        print(type(e))
        print(e)

main()