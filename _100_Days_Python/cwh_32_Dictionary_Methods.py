# # info = {'name':'Karan', 'age':19, 'eligible':True}

# # print(info.items())
# # for key, value in info.items():
# #   print(f"The value corresponding to the key {key} is {value}") 



# dict = {"name":"aditya", 
#     "surname":"jadhav", 
#     "age":202,
#     "result":True}
# print(dict["name"]) # --------> this thows error when vlaue is not exist 
# print(dict.get("name"))# --------> this not thows error print noll when vlaue is not exist 
# print(dict.keys())
# print(dict.values())

# for d in dict.keys():
#     print(f"the key is {d} and corresponding vlaue is {dict[d]}")  #-----> this print vlaues in odered seri.

 

# print(dict.items())
# for key, value in dict.items():
#   print(f"The value corresponding to the key {key} is {value}") 

def dit(self, info):
    print(info)


dit(info = {'name':'Karan', 'age':19, 'eligible':True})