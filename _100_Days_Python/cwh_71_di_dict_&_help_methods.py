class meth1:
    def __init__(self ,name, age):
        self.name =name
        self.age=age
    def emp(pyt):
        print(f"name is {pyt.name} and age is {pyt.age}")
        
m1= meth1("Adi",19)
m1.emp()
print(dir(meth1))  #The dir() function returns a list of all the
#  attributes and methods (including dunder methods) available for 
#  an object. It is a useful tool for discovering what you can do with an object. 

print(m1.__dict__)   #__dict__: The __dict__ attribute returns a dictionary 
# representation of an object's attributes. It is a useful tool for introspection.

print(help(meth1))  #help(): The help() function is used to get help 
# documentation for an object, including a description of its attributes and method

# list = [10,12,0,1,2012]
# print(dir(list))
