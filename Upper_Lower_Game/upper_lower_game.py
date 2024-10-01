# This is the upper lower game .You have guess which entity among the two has more followers.
#Aditya Kumar Roy

import random
import game_database
import os

def account(account):
    name = account["name"]
    description = account["description"]
    country = account["Country"]
    return f"{name},a {description},{country}"
account_2 = random.choice(game_database.data)

def compare(x,y,z):
    if y<z:
        if x == 1:
            return False
        else:
            return True
    else :
        if x ==1:
            return True
        else :
            return False

flag = True
while flag :
    account_1 = account_2
    account_2 = random.choice(game_database.data)
    while account_1 == account_2:
        account_2 = random.choice(game_database.data)
    print(f"Compare 1:{account(account_1)}")
    print("""
            ##  ##    ####   
            ##  ##   ##  ##  
            ##  ##   ##      
            ##  ##    ####   
            ##  ##       ##  
            ####    ##  ##  
            ##      ####   
                        """)
    print(f"Compare 2:{account(account_2)}")
    follower_1 = account_1["follower_count"]
    follower_2 = account_2["follower_count"]
    guess = input("Who has more follower? Type 1 or 2:")
    is_correct = compare(x=guess,y=follower_1,z=follower_2)
    os.system('cls')
    score = 0
    final_score = 0
    if is_correct:
        score += 1
        print("You are correct ...your score is:",score)
        flag = True
    else:
        flag = False
        print("You are wrong...your score is:",score)
    final_score += score

print("Total score : ",final_score)
