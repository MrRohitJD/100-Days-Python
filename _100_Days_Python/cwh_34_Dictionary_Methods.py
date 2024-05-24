ep ={101 : "aditya",
    102 : "rohit",
    105 : "adi"}
print(ep.values()) 
print(ep.keys())


# ------------update()---------------
# ep.update({110: "adu"})
# print(ep.keys(), ep.values())


# ---------------clear()-------------
# ep.clear()
# print(ep)

# ---------------pop()-------------
# ep.pop(105)
# print(ep)

# --------------popitem()-----------
# ep.popitem()
# print(ep)  #---> popitem use for delete item from end.

# ------------del--------------
# del ep[101]
# print(ep)

# print(ep)
# del ep
# print(ep)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
