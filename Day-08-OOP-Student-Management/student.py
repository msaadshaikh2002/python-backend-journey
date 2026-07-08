class Student:
    # Class Attribute
    school_name = "ABC Public School"

    # Constructor
    def __init__(self, name, roll_no, age, marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks

    # Instance Method
    def display_student(self):
        print("\n----- Student Details -----")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Age      : {self.age}")
        print(f"Marks    : {self.marks}")

    # Instance Method
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    # Instance Method
    def update_marks(self, new_marks):
        if Student.is_valid_marks(new_marks):
            self.marks = new_marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Marks should be between 0 and 100.")

    # Class Method
    @classmethod
    def show_school_name(cls):
        print(f"School Name: {cls.school_name}")

    # Static Method
    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100