class names:
    def __init__(self, name) -> None:
        self.name

    def show(self):
        print(f"this is name {self.name}")

class IDs:
    def __init__(self , id) -> None:
        self.id =id

    def shows(self):
        print(f"The ID is {self.id}")
        
class employee(names , IDs):
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

o = employee("Rohit" , 12)
print(o.name)
print(o.id)
# o.name()
# o.id()
o.show()      
o.shows()  
        
