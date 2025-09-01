from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade
from faker import Faker
import random
from datetime import datetime

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/students_db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=f"Subject {i}", teacher=random.choice(teachers)) for i in range(1, 8)]
session.add_all(subjects)
session.commit()

students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(40)]
session.add_all(students)
session.commit()

for student in students:
    for _ in range(random.randint(10, 20)):
        grade = Grade(
            student=student,
            subject=random.choice(subjects),
            grade=random.randint(5, 12),
            date=fake.date_this_year()
        )
        session.add(grade)

session.commit()
session.close()
