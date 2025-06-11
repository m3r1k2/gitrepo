import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20),
        age INTEGER,
        major VARCHAR(100)
        )
    CREATE TABLE courses(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(40),
        instructor VARCHAR(25)
        )
''')
cursor.execute('''
    CREATE TABLE students_courses
    student_id INTEGER PRIMARY KEY,
    course_id INTEGER PRIMARY KEY,
    FOREIGN KEY (student_id) REFERENCES students(id)
    FOREIGN KEY (course_id) REFERENCES courses(id) 
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
    cursor.execute("INSERT INTO student_courses (course_id, student_id) values(?,?)", course_id,student_id)
    conn.commit()

def sdutents_in_course(course_id):
    cursor.execute("SELECT students.id, students.name FROM students JOIN student_courses"
                   "ON students.id = student_courses.student_id WHERE students_course.course.id = ? ", (course_id))
    res = cursor.fetchall()
    for r in res :
        print(f"ID:{r[0]}, Name{r[1]}")


while True:
    print("/n1. Додати нового студента")
    print("2. Додати новий курс ")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зарегіструватись на курс")
    print("6. Показати студентів на курсі")
    print("7. Вихід")

    choose = int(input("Вибери дію від 1 до 7"))
    if choose == 1:
        add_student()

    elif choose == 2:
        add_course()

    elif choose == 3:
        show_students()

    elif choose == 4:
        show_course()

    elif choose == 5:
        register_course()

    elif choose == 6:
        sdutents_in_course()

    elif choose == 7:
        break