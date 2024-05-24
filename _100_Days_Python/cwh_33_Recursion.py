
# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)    ------------------> this is imp for knowing 
# how factorial(n - 1) is work inside the copmuter





# def factorial(n):
#     if n==0 or n==1:
#          return 1
#     else:
#          return n*factorial(n-1)

# print(factorial(3))


def fibb(i):
    if (i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return fibb(i-1)+fibb(i-2)

print(fibb(6))

