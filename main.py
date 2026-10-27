students = []

try:
    with open("students.txt") as f:
        for line in f:
            students.append(line.strip())
except FileNotFoundError:
    pass

def save():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(s + "\n")

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Delete student")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        students.append(name)
        save()
        print("Student added")
    elif choice == "2":
        for i in range(len(students)):
            print(i + 1, students[i])
    elif choice == "3":
        number = int(input("Enter number to delete: "))
        if 1 <= number <= len(students):
            students.pop(number - 1)
            save()
            print("Student deleted")
        else:
            print("Wrong number")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
