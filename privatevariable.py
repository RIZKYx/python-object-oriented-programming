class hero:
    #class variable

    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #variable instance private
        self.__private = 'private'
        #variable instance protected
        self._protected = "protected" 
        
lina = hero('lina',100)


print(lina.__dict__)
print(hero.__dict__)
print(hero.__privatejumlah)

