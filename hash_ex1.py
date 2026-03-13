# CHAPTER 6 EXERCISE 1mple!

# Student Grade Lookup Program

# Initial data
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

while True:

    print("\nMenu:")
    print("1 - Add or update student grade")
    print("2 - Search student grade")
    print("3 - Print all students and grades")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        grades[name] = grade
        print("Grade added/updated successfully.")

    elif choice == "2":
        name = input("Enter student name to search: ")

        if name in grades:
            print(name, "has grade", grades[name])
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in grades.items():
            print(name, ":", grade)

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")