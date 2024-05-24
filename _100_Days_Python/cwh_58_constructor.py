class person:
    def __init__(self , n, o):
        print(f"this is constracter  {n}  {o}")
        self.name= n
        self.occupetion= o

    def info(self):
        print(f"name is {self.name} and my occupetion is {self.occupetion}")

a=person("rohit", '"coder"')
b=person("aditya", "admin")
# a.name= "aditya"
# a.occupetion ="HR"

# b.name ="rohit"
# b.occupetion ="Admin"

a.info()
# b.info()