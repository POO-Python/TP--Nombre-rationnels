class Ratio(object):
    
    #Constructeurs
    def __init__(self, numerateur, denominateur):

        if isinstance(numerateur, int) == False  or isinstance(denominateur, int) == False:
            raise ValueError
        elif denominateur == 0:
            raise ZeroDivisionError
        else:
            self.numerateur = numerateur
            self.denominateur = denominateur

    #Méthodes

    def __str__ (self):

        return str(self.numerateur) +  " / " + str(self.denominateur)

    #Getters
    @property
    def numerateur (self):
        return self.__numerateur

    @property
    def denominateur (self):
        return self.__denominateur

    #Setters
    @numerateur.setter
    def numerateur(self, value):
        self.__numerateur = value

    @denominateur.setter
    def denominateur(self, value):
        self.__denominateur = value




