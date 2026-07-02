book = {}

def show_menu():
    input_ = input("""\n\n --- CONTACT BOOK MENU ---

1 - Add contact
2 - View contacts
3 - Search contact
4 - Delete contact
5 - Exit
\n
Enter Your Choice: """)

    return input_

def add_contact():
    name = input("Enter Name: ").title()
    number = int(input("Enter Number: "))
    
    book[name] = number
    print("Contact added successfully!")

def view_contacts():
    if not book:
        print("No contacts found.")
        return
        
    for name,number in book.items():
        print(name,":",number)

def search_contact():
    name = input("Enter name to search: ").title()
    
    if name in book:
        print(name, ":", book[name])
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").title()
    
    if name in book:
        del book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        input_ = show_menu()
        if input_ == "1":
            add_contact()
        elif input_ == "2":
            view_contacts()
        elif input_ == "3":
            search_contact()
        elif input_ == "4":
            delete_contact()
        elif input_ == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

main()
