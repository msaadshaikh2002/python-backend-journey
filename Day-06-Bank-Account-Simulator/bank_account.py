balance = 1000.00

def show_menu():
    print("========== BANK ACCOUNT ==========")
    print("\n1. Check Balance")
    print("\n2. Deposit Money")
    print("\n3. Withdraw Money")
    print("\n4. Exit")

    choice = input("\nSelect option: ")

    return choice

def check_balance():
    global balance
    print(f"Your Balance is: ₹{balance}")

def deposit_money():
    global balance
    try:
        add = float(input("Enter Amount to Deposit: "))
        if add <=0:
            print("Enter valid amount.")
        else:
            balance += add
            print(f"New Balance: {balance:.2f}")
            
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    
def withdraw_money():
    global balance

    try:
        substract = float(input("Enter Amount to Withdraw: "))
        
        if substract <= 0:
            print("Enter valid amount.")
        elif substract > balance:
            print("Insufficient balance.")
        else:
            balance -= substract
            print(f"New Balance: {balance:.2f}")
    
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def menu():
    while True:
        choice = show_menu()
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you for using Bank Account Simulator!")
            break
        else:
            print("Invalid input")

menu()