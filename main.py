import csv
import os

FILE_NAME = "students.csv"

# Create file with header if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll", "Name", "Course", "Year"])


# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, course, year])

    print("\n✔ Student Added Successfully!\n")


# View all students
def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        print("\n--- Student Records ---")
        for row in reader:
            print(row)
    print()


# Search student
def search_student():
    roll = input("Enter Roll to Search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("\n✔ Student Found:", row, "\n")
                found = True
                break

    if not found:
        print("\n❌ Student Not Found!\n")


# Update student
def update_student():
    roll = input("Enter Roll to Update: ")
    updated = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("Enter new details:")
                name = input("New Name: ")
                course = input("New Course: ")
                year = input("New Year: ")
                rows.append([roll, name, course, year])
                updated = True
            else:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("\n✔ Record Updated Successfully!\n")
    else:
        print("\n❌ Roll Number Not Found!\n")


# Delete student
def delete_student():
    roll = input("Enter Roll to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                deleted = True
            else:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("\n✔ Student Deleted Successfully!\n")
    else:
        print("\n❌ Roll Number Not Found!\n")


# Menu-driven program
def menu():
    initialize_file()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM (Simple CSV Version) =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("\n❌ Invalid choice! Try again.\n")


menu()