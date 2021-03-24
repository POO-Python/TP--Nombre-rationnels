class Ratio(object):
    
    #Constructeurs
    def __init__(self, denominateur, numerateur):

        if isinstance(denominateur, int) == False  or isinstance(numerateur, int) == False:
            raise ValueError
        else:
            self.denominateur = denominateur
            self.numerateur = numerateur


    #Getters
    @property
    def denominateur (self):
        return self.__denominateur

    @property
    def numerateur (self):
        return self.__numerateur


    #Setters
    @denominateur.setter
    def denominateur(self, value):
        self.__denominateur = value

    @numerateur.setter
    def numerateur(self, value):
        self.__numerateur = value




