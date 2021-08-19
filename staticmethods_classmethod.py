class hero:
    #private class varriable
    __jumlah = 0
    def __init__(self,name):
        self.__name = name
        hero.__jumlah += 1

    #method ini hanya berlaku untuk object
    def getJumlah(self):
        return hero.__jumlah
    
    #method ini tidak berlaku untuk object tapi berlaku untuk class
    def getJumlah1():
        return hero.__jumlah

    #methods static (decorator) nempel ke object dan classnya
    @staticmethod
    def getJumlah2():
        return hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

sniper = hero('sniper')
print(hero.getJumlah2())
rikimaru = hero('rikimaru')
print(sniper.getJumlah2())
drowranger = hero('drowranger')
print(hero.getJumlah3()) 