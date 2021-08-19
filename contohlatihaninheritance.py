class Team:
    def setteam(self,team):
        self.team = team

    def showteam(self):
        print(self.team)

class Tipe_hero:
    def settipe(self,tipe):
        self.tipe = tipe

    def showtipe(self):
        print(self.tipe)

class Hero(Team,Tipe_hero):
    
    def __init__(self,name,health):
        self.name = name
        self.healrh = health

ucup = Hero('ucup',100)
ucup.setteam('merah')
ucup.settipe('cundang')

ucup.showteam()
ucup.showtipe()