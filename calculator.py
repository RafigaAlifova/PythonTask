print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
try:
    choice = int(input("Enter choice(1/2/3/4): "))
    if choice in (1,2,3,4):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(num1, "+", num2, "=", num1+num2)

        elif choice == 2:
            print(num1, "-", num2, "=", num1-num2)

        elif choice == 3:
            print(num1, "*", num2, "=", num1*num2)

        elif choice == 4:
            print(num1, "/", num2, "=", num1/num2)
    else:
        print("Enter number between 1 and 4!")           
except ValueError as Error:
    print("Invalid Input. Enter only number!")
    print("Original exception message: ",Error)
except ZeroDivisionError as Error:
    print("Don't divide by zero")
    print("Original exception message: ",Error)