a = int(input("enter the number"))
if(a<50 or a>20):
    print("hello")
    raise ValueError("Value should be between 20 and 50")
