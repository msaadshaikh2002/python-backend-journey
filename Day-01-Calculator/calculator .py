print("===== Python Calculator =====")
print("")
print("What you want to do?")
value = int(input("1 - Addition\n2 - Substraction\n3 - Multiplication\n4 - Division\n\nEnter: "))

if value > 0 and value < 5:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if value == 1:
        print("Ans:",num1+num2)
    elif value == 2:
        print("Ans:",num1-num2)
    elif value == 3:
        print("Ans:",num1*num2)
    elif value == 4:
        if num2 == 0:
            print("Ans:","Cannot Divide by Zero")
        else:
            print("Ans:",num1/num2)
else:
    print("Invalid Input")
    