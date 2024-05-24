import random
import string

opt=input("    1: Code    2: Decode\n.= ")
print(type(opt))
if(opt=="1"):
    i =str(input("enter message here  "))
    app = i[1:]
    one = i[0]
    full = (app+one)
    letters = string.ascii_lowercase
    result_str1 = ''.join(random.choice(letters) for i in range(3))
    result_str2 = ''.join(random.choice(letters) for i in range(3))
    co =result_str1+full+result_str2
    
    print(co)

if(opt=="2"):
    j =str(input("Enter your code massege here "))
    fir = j[3:-4]
    sec =  j[-4]
    print("decoded message is = ",sec+fir)
    
