class data:
    name = "defualt"
    ocupation = "software dev"  # this is defualt values
    mob_num = "null"
    def info(self):
        print(f"{self.name} and occupation is { self.ocupation} ")

a=data()
b=data()
# print(a.name ,a.ocupation) 


#  this for defalut values 
# ji= a.name ="aditya"
# ji1 =a.ocupation = "web dev"
# # print(ji,ji1)

# ji2= b.name ="mani"
# ji4 =b.ocupation = "khana"
# print(ji,ji2)


# this for method 
a.name="aditya"
a.ocupation ="hr"

b.name ="neeta"
b.ocupation="mammy"
b.mob_num="8073413778"

a.name="aditya"
a.ocupation ="hr"

# b.name
# b.ocupation
# b.mob_num

a.info()
b.info()
