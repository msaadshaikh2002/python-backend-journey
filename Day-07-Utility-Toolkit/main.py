import calculator
import converter
from password_generator import password_generator
import greetings


def calculator_menu():
    while True:
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            if choice == "1":
                print("Answer:", calculator.add(num1, num2))

            elif choice == "2":
                print("Answer:", calculator.subtract(num1, num2))

            elif choice == "3":
                print("Answer:", calculator.multiply(num1, num2))

            elif choice == "4":
                print("Answer:", calculator.divide(num1, num2))

            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter valid numbers.")


def converter_menu():
    while True:
        print("\n===== Converter =====")
        print("1. cm_to_meter")
        print("2. meter_to_cm")
        print("3. celsius_to_fahrenheit")
        print("4. fahrenheit_to_celsius")
        print("5. Exit")

        choice = input("Select Operation: ")

        if choice == "5":
            break

        try:
            value1 = float(input("Enter value to convert: "))
        
            if choice == "1":
                print("Answer:", converter.cm_to_meter(value1))
            
            elif choice == "2":
                print("Answer:", converter.meter_to_cm(value1))

            elif choice == "3":
                print("Answer:", converter.celsius_to_fahrenheit(value1))
            
            elif choice == "4":
                print("Answer:", converter.fahrenheit_to_celsius(value1))
            
            else:
                print("Invalid choice.")
                  
        except ValueError:
            print("Please enter valid numbers.")


def greetings_menu():
    while True:
        print("\n======== Greetings ========")
        print("1. Good Morning")
        print("2. Good Evening")
        print("3. Welcome")
        print("4. Exit")

        choice = input("Select Greeting: ")
        
        if choice == "4":
            break
        
        elif choice not in ["1", "2", "3"]:
            print("Invalid choice.")
            continue

        name = input("Your Name Please: ")
        
        if choice == "1":
            print("Answer: ",greetings.good_morning(name))

        elif choice == "2":
            print("Answer: ",greetings.good_evening(name))
        
        elif choice == "3":
            print("Answer: ",greetings.welcome(name))


def password_generator_menu():
    while True:
        print("\n===== Password Generator =====")
        print("1. Generate Password")
        print("2. Exit")

        choice = input("Select Option: ")

        if choice == "1":
            try:
                length = int(input("Enter password length: "))
                print("Generated Password:", password_generator(length))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            break

        else:
            print("Invalid choice.")



def show_menu():
    while True:
        print("\n========== Utility Toolkit ==========")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Password Generator")
        print("4. Greetings")
        print("5. Exit")

        choice = input("Select Option: ")

        if choice == "1":
            calculator_menu()

        elif choice == "2":
            converter_menu()

        elif choice == "3":
            password_generator_menu()

        elif choice == "4":
            greetings_menu()

        elif choice == "5":
            print("Thank you for using Utility Toolkit!")
            break

        else:
            print("Invalid Choice.")


show_menu()