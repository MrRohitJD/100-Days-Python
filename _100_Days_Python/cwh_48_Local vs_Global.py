a= 10;
print(a)

def hello():
    global a;
    a=121
    print("this is a",a)
    b= 90
    print("this is b", b)

hello();
print("this is a outside of def",a) #------------this is globel viraable
# print(b)  #------------this is local viraable