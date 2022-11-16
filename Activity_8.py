def addition():
    num3 = num1 + num2
    return num3
def subtraction():
    num3 = num1 - num2
    return num3
def multiplication():
    num3 = num1 * num2
    return num3
def division():
    num3 = num1/num2
    return num3
while (1):
    
    n = int(input("Press 1 to continue and To Exit Press 2 : "))
    if n == 1:
        a = input("Enter your choice (+,-,*,/) : ")
        num1 = int(input("Enter the 1st number = "))
        num2 = int(input("Enter the 2nd number = "))
        if (a == '+'): 
            print("The additon of two number = ", addition())
        elif (a == '-'):
            print("The subtraction of two number = ", subtraction())
        elif (a == '*'):
            print("The multiplication of two number = ", multiplication())
        elif (a == '/'):
            print("The division of two number = ", division())
        else:
            print("Enter the valid choice...!!!")
    else:
        print("Exiting...Thank you")
        exit()