@staticmethod
def add(x,y):
    return x+y

class math:
    def sub(self ,a,b):
        c=a-b
        print("sub ",c)

    @staticmethod
    def add(x,y):
        return x+y

a=math()
a.sub(20,30)

print(a.add(2000,1000))


print(add(5,2))