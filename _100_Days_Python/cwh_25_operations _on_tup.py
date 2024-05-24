# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# print(temp)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)



tuple1 = (0, 1, 2, 3,3,2,3, 1, 3, 2)
# rev= tuple1.count(2)
# print(rev)
# rev = tuple1.index(1)
# print(rev)
rev1 = tuple1.index(1,4,9)
print(rev1)