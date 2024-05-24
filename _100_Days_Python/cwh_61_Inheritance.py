class emp:
    def __init__(self, na,id) :
        self.name = na
        self.id=id
        
    def info(self):
        print(f"name is {self.name} and id is {self.id}")
class manager(emp):
    def man(self,name):
        print(f"this is manager {self.name}")



obj =emp("rohit",45)
obj.info()

obj1 =emp("aditya",40)
obj1.info()

m= manager("rohit",1)
m.man("adityaaa")