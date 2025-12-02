import mysql.connector

# --------------------------
# DATABASE CONNECTION
# --------------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql275@",   # Change if needed
        database="student_db"
    )
    cursor = conn.cursor()
    print("Database connected successfully!")

except mysql.connector.Error as err:
    print("Connection error:", err)
    exit()


# --------------------------
# LOGIN FUNCTION
# --------------------------
def login():
    while True:
        print("\n----- LOGIN -----")
        username = input("Enter username: ")
        password = input("Enter password: ")

        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print("\nLogin successful! Welcome,", username)
            return True
        else:
            print("\nInvalid username or password! Try again.\n")


# --------------------------
# 1. ADD STUDENT
# --------------------------
def add_student():
    roll = input("Enter Roll: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    query = "INSERT INTO students (roll, name, age, grade) VALUES (%s, %s, %s, %s)"
    values = (roll, name, age, grade)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Student added successfully!\n")
    except mysql.connector.Error as err:
        print("Error:", err)


# --------------------------
# 2. VIEW STUDENTS
# --------------------------
def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    for row in data:
        print(row)


# --------------------------
# 3. SEARCH STUDENT
# --------------------------
def search_student():
    roll = input("Enter Roll to search: ")

    query = "SELECT * FROM students WHERE roll = %s"
    cursor.execute(query, (roll,))
    data = cursor.fetchone()

    if data:
        print(data)
    else:
        print("No student found!")


# --------------------------
# 4. DELETE STUDENT
# --------------------------
def delete_student():
    roll = input("Enter Roll to delete: ")

    query = "DELETE FROM students WHERE roll = %s"
    cursor.execute(query, (roll,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("No student found!")


# --------------------------
# 5. UPDATE STUDENT
# --------------------------
def update_student():
    roll = input("Enter Roll to update: ")

    name = input("New Name: ")
    age = input("New Age: ")
    grade = input("New Grade: ")

    query = "UPDATE students SET name=%s, age=%s, grade=%s WHERE roll=%s"
    values = (name, age, grade, roll)

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("No student found!")


# --------------------------
# MAIN PROGRAM STARTS
# --------------------------
if login():  # LOGIN FIRST
    while True:
        print("\n----- Student Management System (MySQL) -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Try again.")
