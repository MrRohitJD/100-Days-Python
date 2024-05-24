import os;

file = os.listdir("cwh_75_Exercise_7_Solutio")
# print(file)
i=1
for files in file:
    if files.endswith(".png"):
        print(files)
        os.rename(f"cwh_75_Exercise_7_Solutio/{files}", f"cwh_75_Exercise_7_Solutio/{i}.png")
        i+=1