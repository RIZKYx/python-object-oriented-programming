class hero:
#class variable
    jumlah = 0
    
    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        #instance variable
        self.name=inputname
        self.health=inputhealth
        self.power=inputpower
        self.armor=inputarmor
        hero.jumlah += 1
        print('membuat hero dengan jumlah '+inputname)
        
        
hero1=hero('sniper',100,10,4)
print(hero.jumlah)
hero2=hero('axe',100,15,1)
print(hero.jumlah)
hero3=hero('exe',1000,100,0)
print(hero.jumlah)



