class Employee:
    def __init__(self, name, salaray):
        self.name= name
        self.salaray= salaray
    @classmethod  #-----------this is also colledd as Class_methods_ ALTERNATIVE CONSTRUCYTORS
    def fromStr(cls, string ): 
        return cls(string.split("_")[0], string.split("_")[1])   

e1 = Employee("aditya",1000000)
print(e1.name,e1.salaray)

string ="Rohit_95000"
e2 =Employee.fromStr(string)   #-----------this is also colledd as Class_methods_ ALTERNATIVE CONSTRUCYTORS
print(e2.name)
print(e2.salaray)

