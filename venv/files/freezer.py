class Freezer:

    types = 0

    def __init__(self,
                 freezer_company="Bosh",
                 volume_of_freezer=70,
                 weight_of_freezer=40,
                 height_of_freezer=180, width_of_freezer=100, how_much_doors=2):
        self.freezer_company = freezer_company
        self.volume_of_freezer = volume_of_freezer
        self.weight_of_freezer = weight_of_freezer
        self.height_of_freezer = height_of_freezer
        self.width_of_freezer = width_of_freezer
        self.how_much_doors = how_much_doors
        Freezer.types=Freezer.types+1

    def __del__(self):
        print ("Destructor is here")

    def __str__(self):
        return "freezer_company= " + self.freezer_company + "\n" \
               + "volume_of_freezer= " + str(self.volume_of_freezer) + "\n" \
               + "weight_of_freezer= " + str(self.weight_of_freezer) + "\n" \
               + "height_of_freezer= " + str(self.height_of_freezer) + "\n" \
               + "width_of_freezer= " + str(self.width_of_freezer) + "\n" \
               + "how_much_doors= " + str(self.how_much_doors) + "\n"

    @staticmethod
    def get_types():
        return print(Freezer.types)

def main():
        standart_freezer = Freezer()
        build_in_freeder = Freezer("Ariston", 50, 20, 150)
        on_the_wall_freezer = Freezer("ElectroLux", 200, 60, 200, 150, 1)

        print (standart_freezer)
        print (build_in_freeder)
        print (on_the_wall_freezer)

        Freezer.get_types()

if __name__ == '__main__':
        main()
