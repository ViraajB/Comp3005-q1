import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="school",
        user="postgres",
        password="postgres"   
    )
#connect code to database

#function to print all student data
def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY student_id;")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    conn.close()

#function to and and print student data

def addStudent(first, last, email, date):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (first, last, email, date)
    )
    conn.commit()
    print("Student added.")
    conn.close()

#function to update student email with id
def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET email=%s WHERE student_id=%s",
        (new_email, student_id)
    )
    conn.commit()
    print("Email updated.")
    conn.close()

#function to delete student using id
def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM students WHERE student_id=%s",
        (student_id,)
    )
    conn.commit()
    print("Student deleted.")
    conn.close()

#main program loop
if __name__ == "__main__":
    while True:
        print("\n1. List students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Quit")
        #call function based on choice
        choice = input("Enter choice: ")

        if choice == "1":
            getAllStudents()

        elif choice == "2":
            f = input("First name: ")
            l = input("Last name: ")
            e = input("Email: ")
            d = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(f, l, e, d)

        elif choice == "3":
            sid = input("Student ID: ")
            new = input("New email: ")
            updateStudentEmail(sid, new)

        elif choice == "4":
            sid = input("Student ID: ")
            deleteStudent(sid)

        elif choice == "5":
            #exit program
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")
