from math import gcd
class Ratio(object):
    
    #Constructeurs
    def __init__(self, numerateur, denominateur):

        #Numérateur ou le Dénominateur ne sont pas des entiers 
        if isinstance(numerateur, int) == False  or isinstance(denominateur, int) == False:
            raise ValueError
        #Dénomiteur est null
        elif denominateur == 0:
            raise ZeroDivisionError
        #La fraction est de la forme a / -b donc on la transforme en a / -b = -a / b
        elif denominateur < 0 and numerateur > 0:
            self.numerateur = -numerateur
            self.denominateur = -denominateur
        #Dans tous les autres cas
        else:
            self.numerateur = numerateur
            self.denominateur = denominateur


    #Méthode qui s'affiche lors d'un print de la classe
    #Elle retourne la fraction rationnel des nombres saisies
    def __str__ (self):

        #La fraction est de la forme a / 1 donc on le transforme en  a / 1 = a
        if self.denominateur == 1 :
            return str(self.numerateur)
        #La fraction est de la forme a / b
        else:
            return str(self.numerateur) +  " / " + str(self.denominateur)

    #Méthode qui permet d'ajouter deux instances de la classe
    #Elle retourne un float
    def __add__ (self, fraction2):

        self.fraction2 = fraction2

        #Appelle de la méthode pour simplifier notre fraction
        fraction_simplifiee_1 = self.fraction_a_simplifier(self.numerateur, self.denominateur)
        fraction1_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction1_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        #Appelle de la méthode pour simplifier notre fraction 
        self.fraction_a_simplifier(fraction2.numerateur, fraction2.denominateur)
        fraction2_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction2_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        #Appelle de la méthode pour ajouter notre fraction

        calcul = self.ajouter_fraction(fraction1_simplifiee_numerateur, fraction1_simplifiee_denominateur, fraction2_simplifiee_numerateur, fraction2_simplifiee_denominateur)

        return "Résultat de l'addition des deux nombres rationnels saisis : " + calcul[1] + " = " + calcul[0]

    #Méthode qui permet d'ajouter 2 fractions simplifiées
    #Elle retourne la somme des fractions
    def ajouter_fraction (self, num1, den1, num2, den2):

        if den1 != 0 or den2 != 0:
            ad = num1 * den2
            cb = num2 * den1
            bd = den1 * den2

            return str(( ad + cb ) / (bd)), str( ad + cb ) + "/" + str(bd)
         
    #Méthode qui permet de savoir s'il est possible de simplifier une fraction
    def fraction_a_simplifier (self, a, b):

        #On définit le plus grand diviseur commum
        pgcd_numerateur = gcd(a, b)
        pgcd_denominateur = gcd(a, b)

        #On déterminie si la fraction peut-être simplifiée ou non: 
        if pgcd_numerateur ==  pgcd_denominateur and pgcd_numerateur != 1 and pgcd_denominateur != 1:
            #Dans ce cas Oui
            numerateur_fraction_simplifiee = a /  pgcd_numerateur
            denominateur_fraction_somplifiee = b / pgcd_denominateur

            #On retourne un tuple avec soit que le numerateur simplifié 
            if denominateur_fraction_somplifiee == 1 :
                self.frac_simplifiee_numerateur = numerateur_fraction_simplifiee
                self.frac_simplifiee_denominateur = 1
            #On retourne un tuple avec le numérateur et le dénominateur
            else:
                self.frac_simplifiee_numerateur = numerateur_fraction_simplifiee 
                self.frac_simplifiee_denominateur = denominateur_fraction_somplifiee
        else:
            #Dans ce cas Non
            self.frac_simplifiee_numerateur = a
            self.frac_simplifiee_denominateur = b
    

    #Getters
    @property
    def numerateur (self):
        return self.__numerateur

    @property
    def denominateur (self):
        return self.__denominateur
    @property
    def frac_simplifiee_numerateur (self):
        return self.__frac_simplifiee_numerateur
    @property
    def frac_simplifiee_denominateur (self):
        return self.__frac_simplifiee_denominateur

    #Setters
    @numerateur.setter
    def numerateur(self, value):
        self.__numerateur = value

    @denominateur.setter
    def denominateur(self, value):
        self.__denominateur = value

    @frac_simplifiee_numerateur.setter
    def frac_simplifiee_numerateur(self, value):
        self.__frac_simplifiee_numerateur = value

    @frac_simplifiee_denominateur.setter
    def frac_simplifiee_denominateur(self, value):
        self.__frac_simplifiee_denominateur = value




