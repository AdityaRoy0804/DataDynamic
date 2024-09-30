#This is the password generator 
#Aditya Kumar Roy

import random
print("Welcome to the password generator")
num = int(input("how many numbers you want in the password "))
alpha = int(input("how many letters you want in the password"))
sp_ch = int(input("how many special characters you want in the password "))
numbers = ['0','1','2','3','4','5','6','7','8','9']
Alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
         'E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
         'S','T','U','V','W','X','Y','Z']
special = ['!','@','#','$','%','^','&','*','(',')','_','-','+']

password = []
for i in range(0,num):
    a = random.choice(numbers)
    password.append(a)
for i in range(0,alpha):
     b= random.choice(Alpha)
     password.append(b)
for i in range(0,sp_ch):
    c = random.choice(special)
    password.append(c)
random.shuffle(password)

a = " "
for i in password :
    a +=i
print(f"your password :{a}")

