# f=open('cwh_51_methods_of_file_io.txt','r');
# # print(type(f))

# f.seek(12)  #10 bit/charater pude jatay
# print(f.tell())  # seek function kut parent seek kelay the sangtay.
# data= f.read(5)
# print(data)

with open('cwh_51_methods_of_file_io2.txt','w') as f:
    f.write('hello hey i am aditya')
    # f.truncate(12)

with open('cwh_51_methods_of_file_io2.txt','r') as f:
    print(f.read())
