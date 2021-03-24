class Ratio(object):
    
    #Constructeurs
    def __init__(self, denominateur1, denominateur2, numerateur1, numerateur2):
        self.denominateur_1 = denominateur1
        self.denominateur_2 = denominateur2

        self.numerateur_1 = numerateur1
        self.numerateur_2 = numerateur2

    #Getters
    @property
    def denominateur_1 (self):
        return self._denominateur_1

    @property
    def denominateur_2 (self):
        return self.__denominateur_2

    @property
    def numerateur_1 (self):
        return self.__numerateur_1

    @property
    def numerateur_2 (self):
        return self.__numerateur_2

    #Setters
    @denominateur_1.setter
    def denominateur_1(self, value):
        self.__denominateur_1 = value

    @denominateur_2.setter
    def denominateur_2(self, value):
        self.__denominateur_2 = value

    @numerateur_1.setter
    def numerateur_1(self, value):
        self.__numerateur_1 = value

    @numerateur_2.setter
    def numerateur_2(self, value):
        self.__numerateur_2 = value



