# def isnum(a,b):
#   print((a + b) / 2)

# isnum(a=0, b=4)

# def avg(a=9, b=5):
# if you not give the argument values than he gives defualt vlaues a=9 ,b=5
# print((a + b) / 2)
# avg(a=0, )


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


c = average(1, 2, 3, 4, 5)
print(c)


def name(fname, mname, lname):
  print("Hello,", fname, mname, lname)


name(mname="Peter", lname="Wesker", fname="Jade")
