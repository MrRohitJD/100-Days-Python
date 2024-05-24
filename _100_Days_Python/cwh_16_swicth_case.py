a = int(input("Enter your number"))
match a:
    case 0 :
        print("number is zero", a==0)
    case 1:
        print("number is less than teen", 10==88)
    case 2:
        print("number is less than hundred", a==90)
    case _ :
        print("none of the above")            





# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)