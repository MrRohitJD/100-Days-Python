f = open('cwh_49_t.txt','r')
t =f.read()
print(t)
f.close()



# --------------------------append (a)--------------
with open('cwh_49_t.txt','a') as h:
    h.write(" this is wold")

# ----------------------------binary (b): used to handle binary files (images, pdfs, etc).)-------------
bb = open('cwh_49_t.txt','rb')
tt=bb.read()
print(tt)
bb.close() 
    
# -----------------------ext (t):----------------------------------
tx =open('cwh_49_t.txt','rt')
ki =tx.read()
print(ki)
tx.close()