class hero:
    #classvariable
    jumlah_hero = 0

    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor= input
        hero.jumlah_hero += 1

        #void function method tanpa return
    def siapa(self):
        print('namaku adalah ' + self.name)
        #method dengan argumen
    def healthup(self,up):
        self.health += up
        #method dengan return
    def gethealth(self):
        return self.health

hero1= hero('snipe r',100,10,5)
hero2= hero('mario bros',90,5,10)

hero1.siapa()
hero1.healthup(10)

print(hero1.gethealth())