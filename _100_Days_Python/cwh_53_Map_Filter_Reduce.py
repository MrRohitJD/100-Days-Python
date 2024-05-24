# def cube(a):
#     return a*a

# newlist =[2,4,6,8,10,12]
# # new =[]
# # for j in newlist:
# #     new.append(cube(j)) #----- MENTOS JINDGI BELOW
# # print(ne0w)


# # MAP
# newli = list(map(cube,newlist))
# print(newli)



# # FILTER IS NOT INBUILD FUNCTION ;WE SHOULD CREATE METHON FIRST LIKE THIS 
# def todo(x ):
#     return x>20 

# newnewl =list(filter(todo ,newli))
# print(newnewl)




# ------------reduce--------------------
from functools import reduce
def fin(f,g):
    return f+g

list = [8,9,9,8,3,1]
ro = reduce(fin ,list)
print(ro)

# _________USING LAMDA_________
r= lambda x,y:x+y
print(reduce(r,list))




