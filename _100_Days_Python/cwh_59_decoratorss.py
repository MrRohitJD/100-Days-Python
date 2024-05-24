def gitu(g):
    def f(*arg, **args,):
        print("this is morning")
        g(*arg, **args)
        print("this is nihht")
    return f

@gitu
def hello():
    print("hello")
@gitu
def add(a,b,c):
    print("add is = ", a+b+c)

hello()
add(45,5)




def greed(fx):
    def fxx(*arg ,**argument):   #----- *arg ,**argument this for when we pass argument is method
        print("this first")
        fx(*arg ,**argument)           #----- *arg ,**argument this for when we pass argument is method
        print("this is last")
        # fx()
        # print("this is end of the last")
    return fxx

@greed
def hello():
    print("hello")


@greed
def add(a,b):
    print("sub = ", a-b)


hello()
add(8,2)
