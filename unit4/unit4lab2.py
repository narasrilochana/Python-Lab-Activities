"""Lab 2 : 
Develop a Python program to manage student records using a text file named students.txt.
The program should provide the following options:
1. Add a new student record.
2. Display all student records.
3. Exit the program.
Each student record should contain:
- Roll Number
- Student Name
- Marks
The program should store student details in a file so that the records remain available even after the program is closed."""

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")

    print("Student record added successfully!")


def display_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.")
            else:
                print("\nStudent Records:")
                for record in records:
                    print(record.strip())

    except FileNotFoundError:
        print("No student records found.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.")