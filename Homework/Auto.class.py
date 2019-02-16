class Auto:

    def __init__(self, marka, model, obiemDvyguna, maksspeed, vaga, kikoMist, rikVypusku):
        self.marka = marka
        self.model = model
        self.obiemDvyguna = obiemDvyguna
        self.maksspeed = maksspeed
        self.vaga = vaga
        self.kikoMist = kikoMist
        self.rikVypusk = rikVypusku

    def show_auto(self):
        discription = "Marka: " + str(self.marka)
        discription += "\nModel is : " + str(self.model)
        discription += "\nObiemDvyguna is :" + str(self.obiemDvyguna)
        discription += "\nMaksspeed is : " + str(self.maksspeed)
        discription += "\nVaga is : " + str(self.vaga)
        discription += "\nKikoMist is : " + str(self.kikoMist)
        discription += "\nRikVypusku is :" + str(self.rikVypusk)
        print(discription)

    def VidcrutuMashuny(self):
        print("Vidcruto")

    def Zakrutu(self):
        print("Zakruto")

    def Zavesty(self):
        print("Zavedeno")

    def Zaglushutu(self):
        print("Zaglusheno")

    def VklFaru(self):
        print("Faru On")

    def UnvklFaru(self):
        print("Faru Off")

    def OpenBagashnuk(self):
        print("BagashnukOpen")

    def setObiemDviguna(self, obiem):
        self.obiemDvyguna = obiem

    def getObiemDviguna(self):
        return self.obiemDvyguna

    def setVaga(self, vaga):
        self.vaga = vaga

    def getVaga(self):
        return self.vaga

    def setMarka(self, marka):
        self.marka = marka

    def getMarka(self):
        return self.marka

# ---------------------------------------------------------------

myAuto = Auto("Mercedes", "cls", 225, 297, "2t", 4, 2017)
myAuto.show_auto()
myAuto.Zavesty()

myAuto.setObiemDviguna(300)

print(myAuto.getObiemDviguna())

myAuto.setVaga(111)
print(myAuto.getVaga())
