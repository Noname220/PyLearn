class Soldaten:
    def __init__(self,name,uron):
        self.name = name
        self.uron = uron
        self.xp = 100

    def show_Soldaten(self):
        discription = (self.name +" Xp is "+ str (self.xp) +" Uron is "+ str (self.uron))
        print(discription)


mySoldaten = Soldaten("Kulak",25)
mySoldaten2 = Soldaten("Bochka",20)

mySoldaten.show_Soldaten()
mySoldaten2.show_Soldaten()

