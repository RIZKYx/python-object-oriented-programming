class hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showinfo(self):
        print('{} dengan health: {}'.format(self.name,self.health))

class hero_intellegent(hero):
    def __init__(self,name):
        #hero.__init__(self,name,100)
        super().__init__(name,100)
        super().showinfo()

class hero_strength(hero):
    def __init__(self,name):
        #hero.__init__(self,name,200)
        super().__init__(name,200)
        super().showinfo()

lina = hero_intellegent('lina')
axe = hero_strength('axe')
