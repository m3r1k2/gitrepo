import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        age INTEGER,
        major VARCHAR(100)
        )
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(40),
        instructor VARCHAR(25)
        )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students_courses(
    student_id INTEGER ,
    course_id INTEGER ,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id) 
    )
''')

def add_student(name, age, major):
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    conn.commit()
def add_course(course_name, instructor):
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (course_name, instructor))
    conn.commit()
def show_students():
    cursor.execute("SELECT * from students")
    for row in cursor.fetchall():
        print(row)

def show_course():
    cursor.execute("SELECT * from courses")
    for row in cursor.fetchall():
        print(row)



def register_course(course_id, student_id):
    cursor.execute("INSERT INTO students_courses (student_id, course_id) VALUES (?,?)", (student_id, course_id))
    conn.commit()

def students_in_course(course_id):
    cursor.execute("SELECT students.id, students.name FROM students JOIN students_courses"
                   "ON students.id = students_courses.student_id WHERE students_courses.course.id = ? ", (course_id))
    res = cursor.fetchall()
    for r in res :
        print(f"ID:{r[0]}, Name{r[1]}")


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс ")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зарегіструватись на курс")
    print("6. Показати студентів на курсі")
    print("7. Вихід")

    choose = int(input("Вибери дію від 1 до 7"))
    if choose == 1:
        name = input("Ім'я студента:")
        age = int(input("Вік:"))
        faculty = input("Факультет:")
        add_student(name, age, faculty)

    elif choose == 2:
        name = input("Назва курсу: ")
        instructor = input("Викладач: ")
        add_course(name, instructor)

    elif choose == 3:
        show_students()

    elif choose == 4:
        show_course()

    elif choose == 5:
        student_id = int(input("ID студента: "))
        course_id = int(input("ID курсу: "))
        register_course(student_id, course_id)

    elif choose == 6:
        course_id = int(input("ID курсу: "))
        students_in_course(course_id)

    elif choose == 7:
        break
        conn.close()