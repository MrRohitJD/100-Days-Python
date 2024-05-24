class vector :
    def __init__(self, x,y,z):
        self.x=x;
        self.y=y;
        self.z=z;
    def __str__(self) :
        return f"{self.x}x + {self.y}y + {self.z}z"
    
    
    
    def __add__(self , i):
        return vector(self.x+i.x , self.y+i.y ,self.z+i.z) 
    
    
v1 = vector(1,2,3)
v2 = vector(4,5,6)
print(v1)
print(v2)
print("---------------")
print(v1+v2)

print(type(v1+v2))
