f=open('cwh_50_method_OfFile_io.txt','r')
i=0
while(True):
    i=i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"mark in {i} is {m1}")
    print(f"mark in {i} is {m2}")
    print(f"mark in {i} is {m3}")
    
    print(line)

# f=open('cwh_50_method_OfFile_io.txt','r')
# i=0
# while(True):
#     i = i+1
#     l =f.readline()
#     if not l:
#         break
#     v =int(l.split(",")[0])
#     b =int(l.split(",")[1])
#     t =int(l.split(",")[2])

#     print(f"mark of{i} is {v}")
#     print(f"mark of{i} is {b}")
#     print(f"mark of{i} is {t}")




