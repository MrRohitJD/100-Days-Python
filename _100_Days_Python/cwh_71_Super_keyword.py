class A:
    def __init__(self, name,age):
        self.name=name
        self.age= age
    def var1(self):
        print(f"this is name  {self.name} and age {self.age}")

class B(A):
    def __init__(self, name, age,Company):
        self.Company =Company
        super().__init__(name, age)
        super().var1()

    def bb(self):
        print(f"this is name {self.name} age {self.age} company {self.Company}")

b=B("adu",10,"ceat")
b.bb()