class hero:

    #private class variable
    __jumlah = 0

    def __init__(self,name,health,attpower,armor):
        self.__name = name
        self.__healthstandar = health
        self.__attpowerstandar = attpower
        self.__armorstandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthmax = self.__healthstandar * self.__level
        self.__attpower = self.__attpowerstandar * self.__level
        self.__armor = self.__armorstandar * self.__level

        self.__health = self.__healthmax

        hero.__jumlah += 1

    @property
    def info(self):
        return '{} level {}: \n\t health = {}/{} \n \t attack = {} \n\t armor = {}'.format(self.__name,self.__level,self.__health,self.__healthmax,self.__attpower,self.__armor)

    @property
    def gainexp(self):
        pass

    @gainexp.setter
    def gainexp(self,addexp):
        self.__exp += addexp
        if(self.__exp >= 100):
            print(self.__name,"level up")
            self.__level += 1
            self.__exp -= 100

        self.__healthmax = self.__healthstandar * self.__level
        self.__attpower = self.__attpowerstandar * self.__level
        self.__armor = self.__armorstandar * self.__level

    def attack(self,musuh):
        self.gainexp = 50

slardar = hero('slardar',100,5,10)
axe = hero('axe',100,5,10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)










         