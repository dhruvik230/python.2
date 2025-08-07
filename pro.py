Record = []

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        subject = input("Enter student subjects: ")

        student = {
            "id": id,
            "name": name,
            "age": age,
            "grade": grade,
            "subject": subject,  
        }

        Record.append(student)
        print("Student added successfully.")

    elif choice == 2:
        if not Record:
            print("No student records found.")
        else:
            for student in Record:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {', '.join(student['subject'])}")

    elif choice == 3:
        id = int(input("Enter student ID to update: "))
        
        for student in Record:
            if student["id"] == id:
                name = input("Enter new student name: ")
                age = int(input("Enter new student age: "))
                grade = input("Enter new student grade: ")
                subject = input("Enter new student subjects (): ")

                student["name"] = name
                student["age"] = age
                student["grade"] = grade
                student["subject"] = subject
                
                print("Student record updated successfully.")
                break
        

    elif choice == 4:
        id= int(input("Enter student ID to delete: "))
        
        for student in Record:
            if student["id"] == id:
                Record.remove(student)
                
                print("Student deleted successfully.")
                break
       

    elif choice == 5:
        print("Exiting program.")
        break
