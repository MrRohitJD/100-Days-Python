class Employee:
    company ="Apple"
    def show(self):
        print(f"this is name {self.name} and {self.company}")
    @classmethod   #---------------------- this @classmethod mhanaje class variable la change krtay. ekda comment out krun pn bhaga.
    def changeCompany(cls, newCompany):
        cls.company=newCompany

    def seeHow(bhendi):
        print(f"this is name {bhendi.name} and {bhendi.company}")

e = Employee()
# e.show()
e.name = "herry"
e.show()
e.changeCompany("Tesla")
e.show()
e.seeHow()
print(Employee.company)
