class Freezer:

    types = 0

    def __init__(self,
                 freezerCompany="Bosh",
                 volumeOfFreezer=70,
                 weightOfFreezer=40,
                 heightOfFreezer=180, widthOfFreezer=100, howMuchDoors=2):
        self.freezerCompany = freezerCompany
        self.volumeOfFreezer = volumeOfFreezer
        self.weightOfFreezer = weightOfFreezer
        self.heightOfFreezer = heightOfFreezer
        self.widthOfFreezer = widthOfFreezer
        self.howMuchDoors = howMuchDoors
        Freezer.types=Freezer.types+1

    def __del__(self):
        print ("Destructor is here")

    def __str__(self):
        return "freezerCompany: " + self.freezerCompany + "\n" \
               + "volumeOfFreezer= " + str(self.volumeOfFreezer) + "\n" \
               + "weightOfFreezer= " + str(self.weightOfFreezer) + "\n" \
               + "heightOfFreezer= " + str(self.heightOfFreezer) + "\n" \
               + "widthOfFreezer= " + str(self.widthOfFreezer) + "\n" \
               + "howMuchDoors= " + str(self.howMuchDoors) + "\n"

    @staticmethod
    def getTypes():
        return print(Freezer.types)

def main():
        standartFreezer = Freezer()
        buildInFreeder = Freezer("Ariston", 50, 20, 150)
        onTheWallFreezer = Freezer("ElectroLux", 200, 60, 200, 150, 1)

        print (standartFreezer)
        print (buildInFreeder)
        print (onTheWallFreezer)

        Freezer.getTypes()

if __name__ == '__main__':
        main()
