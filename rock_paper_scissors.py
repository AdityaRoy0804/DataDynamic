import random
com_score = 0
your_score = 0
print("===================================")
print("This is a rock-paper-scissor game. ")
print("===================================")
while com_score <=5 or your_score<=5 :
    user = input("enter your choice(rock/paper/scissor): ")
    list = ["rock","paper","scissor"]
    com = random.choice(list)
    if(user[0] == 'r' or user[0] == 'R'):
        if(com[0] == 'r' or com[0] == 'R'):
            print(f"computer :{com}")
            print("tie")
        elif(com[0] == 's' or com[0] == 'S'): 
            print(f"computer :{com}")
            print("you won !!")
            your_score+=1
        elif(com[0] == 'p' or com[0] == 'P'):
            print(f"computer :{com}")
            print("you lost..")
            com_score+=1
        else:
            print("invalid input")
    elif(user[0] == 's' or user[0] == 'S'):
        if(com[0] == 's' or com[0] == 'S'):
            print(f"computer :{com}")
            print("tie")
        elif(com[0] == 'p' or com[0] == 'P'):
            print(f"computer :{com}")
            print("you won !!")
            your_score+=1
        elif(com[0] == 'r' or com[0] == 'R'):
            print(f"computer :{com}")
            print("you lost..")
            com_score+=1
        else:
            print("invalid input")
    elif(user[0] == 'p' or user[0] == 'P'):
        if(com[0] == 'p' or com[0] == 'P'):
            print(f"computer :{com}")
            print("tie")
        elif(com[0] == 'r' or com[0] == 'R'):
            print(f"computer :{com}")
            print("you won !!")
            your_score+=1
        elif(com[0] == 's' or com[0] == 'S'):
            print(f"computer :{com}")
            print("you lost..")
            com_score+=1
        else:
            print("invalid input")      
    else:
        print("invalid input")
    if com_score == 5 or your_score == 5:
        break
print("==========================")
print("Your score :",your_score)
print("Computer :",com_score)
if your_score > com_score:
    print("You are the winner !!")
elif your_score < com_score:
    print("You are the loser..")
else:
    print("Game Draw.")