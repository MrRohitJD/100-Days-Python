# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o = Dog("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())



class Phone:
    def __init__(self, name , compony) -> None:
        self.name =name
        self.compony =compony

    def show_detail(self):
        print(f"name : {self.name}")
        print(f"compony :{self.compony}")

class SmartPhone(Phone) :
    def __init__(self, name, model) -> None:
        Phone.__init__(self, name, compony = "Apple")
        self.model = model

    def show_detail(self):
        Phone.show_detail(self)
        print(f"model:{self.model}")

class futures(SmartPhone):
    def __init__(self, name, color) -> None:
        SmartPhone.__init__(self , name, model = "iphone 14")
        self.color =color

    def show_detail(self):
        SmartPhone.show_detail(self)
        print(f"color: {self.color}") 


o= futures("iPhone" , "Black")
o.show_detail()


        

