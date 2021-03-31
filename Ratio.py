from math import gcd
class Ratio(object):
    
    #Constructeurs
    def __init__(self, numerateur, denominateur):
        
        #La fraction est de la forme a / -b donc on la transforme en a / -b = -a / b
        if denominateur < 0 and numerateur > 0:
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
    #Elle retourne une chaine de caractère
    def __add__ (self, fraction2):

        #Appelle de la méthode pour simplifier notre fraction
        self.fraction_a_simplifier(self.numerateur, self.denominateur)
        fraction1_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction1_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        #Appelle de la méthode pour simplifier notre fraction 
        self.fraction_a_simplifier(fraction2.numerateur, fraction2.denominateur)
        fraction2_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction2_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        #Appelle de la méthode pour ajouter notre fraction

        calcul = self.ajouter_fraction(fraction1_simplifiee_numerateur, fraction1_simplifiee_denominateur, fraction2_simplifiee_numerateur, fraction2_simplifiee_denominateur)

        return "\nRésultat de l'addition des deux nombres rationnels saisis : " + calcul[0] + " = " + calcul[1]

    #Méthode qui permet d'ajouter 2 fractions simplifiées
    #Elle retourne la somme des fractions
    def ajouter_fraction (self, num1, den1, num2, den2):

        if den1 != 0 or den2 != 0:

            result_num = num1 * den2 + num2 * den1
            result_dem = den1 * den2

            if result_num < 0 :

                self.fraction_a_simplifier(result_num, result_dem)
                return str( self.frac_simplifiee_numerateur ) + "/" + str(self.frac_simplifiee_denominateur), str( self.frac_simplifiee_numerateur / self.frac_simplifiee_denominateur)

            elif result_dem < 0 :

                self.fraction_a_simplifier(result_num, result_dem)
                return str( -self.frac_simplifiee_numerateur ) + "/" + str(-self.frac_simplifiee_denominateur), str( -self.frac_simplifiee_numerateur  / -self.frac_simplifiee_denominateur)

    #Méthode qui permet de diviser deux instances de la classe
    #Elle retourne une chaine de caractère
    def __truediv__ (self, fraction2):

        #Appelle de la méthode pour simplifier notre fraction
        self.fraction_a_simplifier(self.numerateur, self.denominateur)
        fraction1_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction1_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        #Appelle de la méthode pour simplifier notre fraction 
        self.fraction_a_simplifier(fraction2.numerateur, fraction2.denominateur)
        fraction2_simplifiee_numerateur = int(self.frac_simplifiee_numerateur)
        fraction2_simplifiee_denominateur = int(self.frac_simplifiee_denominateur)

        calcul = self.div_fraction(fraction1_simplifiee_numerateur, fraction1_simplifiee_denominateur, fraction2_simplifiee_numerateur, fraction2_simplifiee_denominateur)

        return "\nRésultat de la division du premier nombre rationnel saisi par le deuxième :b " + calcul[0] + " = " + calcul[1]

    #Méthode qui permet de diviser 2 fractions simplifiées
    #Elle retourne la division des fractions
    def div_fraction (self, num1, den1, num2, den2):

        if den1 != 0 or num2 != 0 or den2 != 0:

            ad = num1 * den2
            bc = den1 * num2

            if ad < 0 and bc < 0 :
                ad = -ad
                bc = -bc

            self.fraction_a_simplifier(ad, bc)

            result = ad / bc

            return str(self.frac_simplifiee_numerateur ) + "/" + str(self.frac_simplifiee_denominateur), str(result)
         
    #Méthode qui permet de savoir s'il est possible de simplifier une fraction
    def fraction_a_simplifier (self, a, b):

        #On définit le plus grand diviseur commum
        pgcd_numerateur = gcd(int(a), int(b))
        pgcd_denominateur = gcd(int(a), int(b))

        #On déterminie si la fraction peut-être simplifiée ou non: 
        if pgcd_numerateur ==  pgcd_denominateur and pgcd_numerateur != 1 and pgcd_denominateur != 1:
            #Dans ce cas Oui
            numerateur_fraction_simplifiee = int(a) /  pgcd_numerateur
            denominateur_fraction_somplifiee = int(b) / pgcd_denominateur

            #On retourne un tuple avec soit que le numerateur simplifié 
            if denominateur_fraction_somplifiee == 1 :
                self.frac_simplifiee_numerateur = int(numerateur_fraction_simplifiee)
                self.frac_simplifiee_denominateur = 1
            #On retourne un tuple avec le numérateur et le dénominateur
            else:
                self.frac_simplifiee_numerateur = int(numerateur_fraction_simplifiee) 
                self.frac_simplifiee_denominateur = int(denominateur_fraction_somplifiee)
        else:
            #Dans ce cas Non
            self.frac_simplifiee_numerateur = int(a)
            self.frac_simplifiee_denominateur = int(b)

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
        #Le Numérateur n'est pas un entier
        if isinstance(value, int) == False:
            raise ValueError
        else:
            self.__numerateur = value

    @denominateur.setter
    def denominateur(self, value):
        #Le Dénominateur n'est pas un entier
        if isinstance(value, int) == False:
           raise ValueError
        #Dénomiteur est null
        elif value == 0:
           raise ZeroDivisionError
        else:
            self.__denominateur = value

    @frac_simplifiee_numerateur.setter
    def frac_simplifiee_numerateur(self, value):
        self.__frac_simplifiee_numerateur = value

    @frac_simplifiee_denominateur.setter
    def frac_simplifiee_denominateur(self, value):
        self.__frac_simplifiee_denominateur = value




