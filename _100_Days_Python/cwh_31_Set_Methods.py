s = {1,4,5,6,7}
q= {2,1,3,4,8,9}
# print(s)
# print(q)
print(s.union(q))
s.update(q)
print(s,q)


# ----------intersection---------
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# ct3 = cities.intersection(cities2)
# print(ct3)

cities.intersection_update(cities2)
print(cities)



# -----------symmetric_difference-----------
x = {1,2,3,6}
y = {2,1,4,6,5,7}
z = y.symmetric_difference(x)
print(z)

y.symmetric_difference_update(x)
print(y)


# -----------difference---------
d1 = {1,2,3,4}
d2 = {3,4,5,6}
d3  = d1.difference(d2)
d4  = d2.difference(d1)
d1.difference_update(d2)
print(d1)
print(d3)
print(d4)

# ----------isdisjoint():------------
i1 = {1,2,3,4}
i2 = {1,2,3,4}
i3 = i1.isdisjoint(i2)
print(i3)

i4 = {1,2,3,4}
i5 = {5,7,8,9}
i7 = i5.isdisjoint(i4)
print(i7)
i5.intersection_update(i4)
print(i5)


# ---------issuperset():-------
# s1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Seoul", "Kabul"}
# s5 = {"Delhi", "Tokyo"}
# s3 = s2.issuperset(s1)
# s4 = s1.issuperset(s5)
# print(s3)
# print(s4)
# Bangalore Delhi Visakhapatnam Hyderabad

# -------------issubset():-----------------
b1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
b2 = {"Delhi", "Madrid"}
print(b2.issubset(b1))