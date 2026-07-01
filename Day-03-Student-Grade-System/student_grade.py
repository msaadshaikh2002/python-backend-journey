def cal_grade(s1,s2,s3,s4,s5):
    total_marks = s1+s2+s3+s4+s5
    average = total_marks / 5
    
    if 90 <= average <= 100:
        grade = "A"
    elif 80 <= average < 90:
        grade = "B"
    elif 70 <= average < 80:
        grade = "C"
    elif 60 <= average < 70:
        grade = "D"
    else:
        grade = "F"
    
    return average,grade

def print_grade(name, average, grade):
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    return f"""Name: {name}
Marks : {average:.2f}
Grade:  {grade}
    
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

def get_input():
    name = input("Your Name Please: ")
    print()
    s1 = int(input("Enter Subject 1 marks: "))
    s2 = int(input("Enter Subject 2 marks: "))
    s3 = int(input("Enter Subject 3 marks: "))
    s4 = int(input("Enter Subject 4 marks: "))
    s5 = int(input("Enter Subject 5 marks: "))

    return name,s1,s2,s3,s4,s5

name,s1,s2,s3,s4,s5 = get_input()

average, grade = cal_grade(s1,s2,s3,s4,s5)

print(print_grade(name,average, grade))

