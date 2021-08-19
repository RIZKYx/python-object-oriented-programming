class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def showinfo(self):
        print('this is class hero')
        print('{} health: {}'.format(self.name,self.health))


class hero_intellegent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    # override
    def showinfo(self):
        print('this is subclass hero')
        print('{} \n\t tipe: intelegent, \n\t health: {}'.format(self.name,self.health))

class hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
    

lina = hero_intellegent('lina')
axe = hero_strength('axe')

lina.showinfo()
axe.showinfo()
