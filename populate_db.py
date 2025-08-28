import psycopg2
from psycopg2.extras import execute_batch
from faker import Faker
import random

DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "postgres_container"
DB_PORT = "5432"

fake = Faker()

GROUPS = ["Group A", "Group B", "Group C"]
TEACHERS = ["John Smith", "Alice Johnson", "Bob Lee", "Emma Davis", "Nick Brown"]
SUBJECTS = ["Math", "Physics", "Chemistry", "Biology", "History", "English", "Art", "Computer Science"]

NUM_STUDENTS = 40
MAX_GRADES_PER_STUDENT = 20

def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        cursor.execute("TRUNCATE TABLE grades RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE students RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE subjects RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE teachers RESTART IDENTITY CASCADE")
        cursor.execute("TRUNCATE TABLE groups RESTART IDENTITY CASCADE")
        conn.commit()

        for group in GROUPS:
            cursor.execute("INSERT INTO groups (name) VALUES (%s)", (group,))

        for teacher in TEACHERS:
            cursor.execute("INSERT INTO teachers (full_name) VALUES (%s)", (teacher,))

        cursor.execute("SELECT id FROM teachers")
        teacher_ids = [row[0] for row in cursor.fetchall()]

        for subject in SUBJECTS:
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)",
                           (subject, random.choice(teacher_ids)))

        cursor.execute("SELECT id FROM groups")
        group_ids = [row[0] for row in cursor.fetchall()]

        for _ in range(NUM_STUDENTS):
            full_name = fake.name()
            group_id = random.choice(group_ids)
            cursor.execute("INSERT INTO students (full_name, group_id) VALUES (%s, %s)",
                           (full_name, group_id))

        cursor.execute("SELECT id FROM students")
        student_ids = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT id FROM subjects")
        subject_ids = [row[0] for row in cursor.fetchall()]

        grades_data = []
        for student_id in student_ids:
            num_grades = random.randint(10, MAX_GRADES_PER_STUDENT)
            for _ in range(num_grades):
                subject_id = random.choice(subject_ids)
                grade = random.randint(60, 100)
                date_received = fake.date_between(start_date='-1y', end_date='today')
                grades_data.append((student_id, subject_id, grade, date_received))

        execute_batch(cursor,
                      "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)",
                      grades_data)

        conn.commit()
        cursor.close()
        conn.close()
        print("Database populated successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
