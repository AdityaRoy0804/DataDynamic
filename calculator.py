def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

op_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    num1 = int(input("Enter first number :"))
    for symbols in op_dict:
        print(symbols)

    flag = True
    while flag :
        op = input("Enter the operations :")
        num2 = int(input("Enter another number :"))
        cal_fun = op_dict[op]
        output = cal_fun(num1,num2)
        print(f"{num1} {op} {num2} = {output}")
        choice = input("Enter 'y' to continue with {output} . Enter 'n' to start new calculation . Enter 'x' to exit. ").lower()
        if choice == "y":
            num1 = output
        elif choice == "n" :
            flag = False
            calculator()
        elif choice == "x" :
            flag = False
        else:
            print("Invalid Input.")