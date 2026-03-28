# Student Management System in Python

import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


students = load_students()


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter student name: ").title()

    if name in students:
        print("Student already exists!")
        return

    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    students[name] = {
        "Maths": maths,
        "Science": science,
        "English": english
    }

    save_students()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")

    for name, marks in students.items():
        average = (marks["Maths"] + marks["Science"] + marks["English"]) / 3

        print(f"\nName: {name}")
        print(f"Maths   : {marks['Maths']}")
        print(f"Science : {marks['Science']}")
        print(f"English : {marks['English']}")
        print(f"Average : {average:.2f}")


def search_student():
    name = input("Enter student name to search: ").title()

    if name in students:
        marks = students[name]

        print("\nStudent Found!")
        print(f"Maths   : {marks['Maths']}")
        print(f"Science : {marks['Science']}")
        print(f"English : {marks['English']}")
    else:
        print("Student not found.")


def update_marks():
    name = input("Enter student name to update: ").title()

    if name not in students:
        print("Student not found.")
        return

    print("1. Maths")
    print("2. Science")
    print("3. English")

    choice = input("Which subject do you want to update? ")
    new_marks = int(input("Enter new marks: "))

    if choice == "1":
        students[name]["Maths"] = new_marks
    elif choice == "2":
        students[name]["Science"] = new_marks
    elif choice == "3":
        students[name]["English"] = new_marks
    else:
        print("Invalid choice")
        return

    save_students()
    print("Marks updated successfully!")


def delete_student():
    name = input("Enter student name to delete: ").title()

    if name in students:
        del students[name]
        save_students()
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def show_topper():
    if not students:
        print("No students found.")
        return

    topper = max(
        students,
        key=lambda name: (
            students[name]["Maths"] +
            students[name]["Science"] +
            students[name]["English"]
        )
    )

    total = (
        students[topper]["Maths"] +
        students[topper]["Science"] +
        students[topper]["English"]
    )

    average = total / 3

    print("\n--- Topper ---")
    print(f"Name    : {topper}")
    print(f"Average : {average:.2f}")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_topper()
    elif choice == "7":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
