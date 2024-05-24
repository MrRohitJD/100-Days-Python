
try:
    a =int(input("Enter your number "))
    print(f"multipitation table of {a} is : ")
    for multi in range(1,11):
        print(f"{a} X {multi}  = {multi*a}")
except:
    print("invalid input")
# print("End of program")
