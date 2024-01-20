
from table import Groups, Students, Disciplines, Teachers, Grades
from faker import Faker
from random import randint, choice
from datetime import datetime
from connect import session
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


NUMBER_STUDENTS = 30
NUMBER_GROUPS = 4
NUMBER_DISCIPLINES = 5
NUMBER_TEACHERS = 3
NUMBER_GRADES = 20

fake_data = Faker()

def add_groups():
    group = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    for name in group:
        session.add(Groups(group_name=name))
    session.commit()


def add_students():
    for _ in range(NUMBER_STUDENTS):
        session.add(Students(students_name=fake_data.name(), groups_id=randint(1, NUMBER_GROUPS)))
    session.commit()


def add_teachers():
    for _ in range(NUMBER_TEACHERS):
        session.add(Teachers(teachers_name=fake_data.name()))
    session.commit()


def add_disciplines():
    disciplines = ['Mathematics', 'Biologi', 'English', 'Statistic', 'History of Ukraine']
    for name in disciplines:
        session.add(Disciplines(disciplines_name=name, teachers_id=randint(1, NUMBER_TEACHERS)))
    session.commit()


def add_grades():
    for stud in range(1, NUMBER_STUDENTS + 1):
        for _ in range(NUMBER_GRADES + 1):
            disciplines = randint(1, NUMBER_DISCIPLINES)
            grade = randint(50, 100)
            date = datetime(randint(2022, 2023), randint(1, 12), randint(1, 28)).date()
            session.add(Grades(students_id=stud, grades=grade, disciplines_id=disciplines, date_grade=date))
    session.commit()


if __name__ == '__main__':
    with session as session:
        add_groups()
        add_students()
        add_teachers()
        add_disciplines()
        add_grades()