a = int(input("number"))
b = int(input("I number"))
for i in range(1,19):
    if(i==b+1):
        break
    print(a,"X",i,"=",a*i)


q = int(input("number"))
for z in range(1,19):
    if(z==10):
        continue  # Skip the alteretion 5X10=50
    print(q,"X",z,"=",q*z)

#  do while loop
x = 0
while True:
  print(x)
  x = x + 1
  if(x%100 == 0):
    break
   
  

