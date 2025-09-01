import argparse
from models import Base, Student, Teacher, Group, Subject, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/students_db')
Session = sessionmaker(bind=engine)
session = Session()

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', required=True)
parser.add_argument('-m', '--model', required=True)
parser.add_argument('--id', type=int)
parser.add_argument('--name')

args = parser.parse_args()

if args.action == 'create' and args.model.lower() == 'teacher':
    new_teacher = Teacher(fullname=args.name)
    session.add(new_teacher)
    session.commit()
    print("Teacher created:", new_teacher.fullname)
