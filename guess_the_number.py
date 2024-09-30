import random

EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 7
HARD_ATTEMPTS = 5

def level_attempts(level):
    if level == "easy":
        return EASY_ATTEMPTS
    elif level == "medium":
        return MEDIUM_ATTEMPTS
    elif level == "hard":
        return HARD_ATTEMPTS
    
def guess_num(x,y):
    if x < num :
        print("Your guess is too low...")
        return False
    elif x> num :
        print("Your guess is too high...")
        return False
    else :
        print("You have made the right guess !!!")
        return True
    
print("==================================")
print("THIS IS THE NUMBER GUESSING GAME ") 
print("==================================")  
print("Let me think of the number between 1 to 50")
num = random.randint(1,50)
level = input("Choose level of difficulty...easy/medium/hard : ").lower()
attempt = level_attempts(level)
while attempt != 0 :
    print(f"You have {attempt} attempts remaining !")
    guess = int(input(" Make a Guess : "))
    correct = guess_num(guess,num)
    if correct == False:
        attempt = attempt - 1
        if attempt != 0:
            print("Make a Guess again.")
    else :
        break
    
if attempt == 0:
    print("No attempts remaining.")
    print("You lost")
    print(f"The correct answer was {num}.")
else :
    print("You Won")