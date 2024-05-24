# ---------------------------Private Access Modifier denoted by(__)---------------
#               -------Private method -------
# class fogg:
#     def __koko(self,name,photo):
#         print(f"{name} and {photo}")

# f=fogg()
# f._fogg__koko("rohit", 14)

#               -------Private method and variable-------

# class fogg1:
#     def __init__(self,name,photo):
#         self.__name=name
#         self.photo = photo

#     def __koko(self):
#         print(f"{self.__name} and {self.photo}")

# f1=fogg1("rohit","haaa")
# print(f1._fogg1__koko())


# ---------------------------Protected Access Modifier denoted by(_)---------------


class fogg1:
    def __init__(self,name,photo):
        self._name=name
        self.photo = photo

    def _koko1(self):
        print(f"{self._name} and {self.photo}")

obj = fogg1("hello",45)
# print(obj._name)     ## -Protected Access Modifier call   obj1.var
print(obj._koko1())  # -Protected Access Modifier call   obj1._funName()
