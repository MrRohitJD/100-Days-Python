import random as r
# comp =[ "Snake", "Water" ,"Gun" ]
comp1 =[0,1,2]
# print(comp1)
count =0    
while(True):
    r.shuffle(comp1)
    zero =comp1[0]
    count+=1

    print("'0' for snake\n'1' for Water\n'2'for Gun")
    player =int(input("your choose  "))
    if player == zero:
        print("------drow-----")

    if player-zero==1 or player-zero==-2:
        print("-------You lose------")

    elif player-zero==-1 or player-zero==2:
        print("**************YOU WIN*************")
        print(comp1[0])
        break
        False
print("total rounds",count)
 











