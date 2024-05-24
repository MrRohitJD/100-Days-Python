l = [11,22,47,1,2,3,4,1,2,2,2,2]
# l.append(0)
# print(l)
# # l.sort()
# # l.sort(reverse=True)
# # l.reverse()
print(l.index(4))
# print(l.count(2))     #---> this is count how many time 2 is repeted



# m=l
# m[0] =999
# print(m) # ------>Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# thats why we use copy funjction
#  m = l.copy()
# print(m)

l.insert(0,1000)
print(l)
# n= [400,500,600,700]
# j=l+n
# print(j)
# l.extend(n)
# print(l)