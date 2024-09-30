# Pizza Cafe Simulator
# Aditya Kumar Roy

print("=========================")
print("Welcome to Pizza Venue")
print("=========================")
a = input("Do you want to have pizza (yes/no)?")
if(a[0] == 'y' or a[0] == 'Y') :
    choice = input("enter the size of the pizza (small/medium/large) :")
    if(choice[0] == 's' or choice[0] == 'S'):
        bill = 100
        pep = input("do you want extra pepperoni (yes/no) :")
        if(pep[0] == 'y' or pep[0] == 'Y'):
             bill = bill + 20
        print(f"The cost of the pizza is : {bill}")
    elif(choice[0] == 'm' or choice[0] == 'M'):
        bill = 200
        pep = input("do you want extra pepperoni (yes/no) :")
        if(pep[0] == 'y' or pep[0] == 'Y'):
             bill = bill + 30
        print(f"The cost of the pizza is : {bill}")
    elif(choice[0] == 'l' or choice[0] == 'B'):
        bill = 300
        pep = input("do you want extra pepperoni (yes/no) :")
        if(pep[0] == 'y' or pep[0] == 'Y'):
             bill = bill + 40
        print(f"The cost of the pizza is : {bill}")
    else:
        print("Wrong input")
    ch = input("do you want extra cheese (yes/no) :")
    if(ch[0] == 'y' or ch[0] == 'Y'):
        bill = bill + 50
    print(f"Total bill : Rs .{bill} /-")
    print("\n Thank You !")

else :
    print("place another order from the menu ")
    
