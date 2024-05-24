import time
localtime = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(localtime)
if(24<hour<12):
    print("Goood morning... sir😀😀")

elif(hour==24):
    print("noon")

elif(hour==12):
    print("noon")

elif(12<hour<17):
    print("Gooood... afternoon....sir😀😀")

elif(17<hour<21):
    print("Goood..evening...sir😀😀")

else:
    print("Good night!!!")

