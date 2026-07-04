import os

filename = "notes.txt"

def add_note():
    text = input("Write here: ")
    
    with open(filename,"a") as file:
        file.write("\n" + text)

    print("Note added successfully.")
        
def view_notes():
    if filename:
        with open(filename,"r") as file:
            for line_no, line in enumerate(file, start = 1):
                print(f"{line_no}. {line.strip()}")
    else:
        print(f"{filename} doesn't exist")
        return
        
def delete_notes():
    filename = "notes.txt"
    confirmation = input("Are you sure (Y/N)? ").upper()
    if confirmation.upper() == "Y":
        with open(filename, "w"):
            pass
        print("All notes deleted.")
    elif confirmation.upper() == "N":
        pass
        
def show_menu():
    print("========== NOTES MANAGER ==========")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")
    choice = input("Enter your choice:")

    return choice

def menu():
    while True:
        choice = show_menu()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Thank you for using Notes Manager!")
            break
        else:
            print("Invalid input")

menu()