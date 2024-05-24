class Animal:
    def __init__(self,name ,species) -> None:
        self.name = name
        self.species =species

    def make_sound(self):
        print("Sound made by the animal")

    def eatFood(self):
        print("mate")

class dog(Animal):
    def __init__(self, name ,breed) -> None:
        Animal.__init__(self ,name, species = "dog")
        self.breed =breed

    def make_sound(self):
        print("Bark!")


# a=Animal("Dogd" , "Dogerman")
# a.make_sound()


d = dog("name", "breed")
d.make_sound()
d.eatFood()

