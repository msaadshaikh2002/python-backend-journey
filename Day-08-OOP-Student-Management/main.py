from student import Student

student = None

while True:
    print("\n========== Student Management ==========")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Update Marks")
    print("4. Calculate Grade")
    print("5. Show School Name")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        if Student.is_valid_marks(marks):
            student = Student(name, roll_no, age, marks)
            print("Student added successfully.")
        else:
            print("Invalid marks! Student not created.")

    elif choice == "2":
        if student:
            student.display_student()
        else:
            print("No student available.")

    elif choice == "3":
        if student:
            new_marks = float(input("Enter New Marks: "))
            student.update_marks(new_marks)
        else:
            print("No student available.")

    elif choice == "4":
        if student:
            print(f"Grade: {student.calculate_grade()}")
        else:
            print("No student available.")

    elif choice == "5":
        Student.show_school_name()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")