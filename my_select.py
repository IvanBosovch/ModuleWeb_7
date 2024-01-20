from sqlalchemy import func, desc
from connect import session
from sqlalchemy import select
from table import Groups, Students, Teachers, Disciplines, Grades

def select_1():
    result = session.query(Students.students_name, func.round(func.avg(Grades.grades), 2).label('avg_grade'))\
        .select_from(Grades).join(Students).group_by(Students.students_id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    result = session.query(Disciplines.disciplines_name, Students.students_name, func.round(func.avg(Grades.grades), 2).label('avg_grade'))\
        .select_from(Grades)\
        .join(Students)\
        .join(Disciplines)\
        .filter(Disciplines.disciplines_id==2)\
        .group_by(Students.students_name, Disciplines.disciplines_name)\
        .limit(1).all()
    return result


def select_3():
    result = session.query(Groups.group_name, Disciplines.disciplines_name, func.round(func.avg(Grades.grades), 2).label('avg_grade'))\
        .select_from(Grades)\
        .join(Students)\
        .join(Disciplines)\
        .join(Groups)\
        .filter(Disciplines.disciplines_id==3)\
        .group_by(Groups.group_name, Disciplines.disciplines_name)\
        .order_by(desc('avg_grade')) \
        .all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grades.grades), 2).label('avg_grade')).select_from(Grades).all()
    return result


def select_5():
    result = session.query(Disciplines.disciplines_name, Teachers.teachers_name).select_from(Disciplines)\
    .join(Teachers)\
    .filter(Teachers.teachers_id==2).all()
    return result


def select_6():
    result = session.query(Students.students_name, Groups.group_name).select_from(Students)\
    .join(Groups)\
    .filter(Groups.groups_id==4).all()
    return result


def select_7():
    result = session.query(Students.students_name, Disciplines.disciplines_name, Groups.group_name, Grades.grades)\
    .select_from(Grades)\
    .join(Students)\
    .join(Groups)\
    .join(Disciplines)\
    .filter(Groups.groups_id==4)\
    .filter(Disciplines.disciplines_id==1)\
    .order_by(Grades.grades).all()
    return result


def select_8():
    result = session.query(Teachers.teachers_name, Disciplines.disciplines_name,func.round(func.avg(Grades.grades), 2).label('avg_grade'))\
    .select_from(Grades)\
    .join(Disciplines)\
    .join(Teachers)\
    .filter(Teachers.teachers_id==3)\
    .group_by(Disciplines.disciplines_name, Teachers.teachers_name)\
    .order_by(desc('avg_grade')).all()
    return result


def select_9():
    result = session.query(Students.students_name, Disciplines.disciplines_name).select_from(Grades)\
    .join(Disciplines)\
    .join(Students)\
    .filter(Students.students_id==22)\
    .group_by(Disciplines.disciplines_id, Students.students_name).all()
    return result


def select_10():
    result = session.query(Students.students_name, Disciplines.disciplines_name, Teachers.teachers_name)\
    .select_from(Grades)\
    .join(Disciplines)\
    .join(Students)\
    .join(Teachers)\
    .filter(Students.students_id==5)\
    .filter(Teachers.teachers_id==3)\
    .group_by(Teachers.teachers_name, Students.students_name, Disciplines.disciplines_name).all()
    return result


if __name__ == '__main__':
    print(select_1()) #Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    print(select_2())  #Знайти студента із найвищим середнім балом з певного предмета.
    print(select_3())  #Знайти середній бал у групах з певного предмета.
    print(select_4())  #Знайти середній бал на потоці (по всій таблиці оцінок).
    print(select_5())  #Знайти які курси читає певний викладач.
    print(select_6())  # Знайти список студентів у певній групі.
    print(select_7())  # Знайти оцінки студентів у окремій групі з певного предмета.
    print(select_8())  # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    print(select_9())  # Знайти список курсів, які відвідує певний студент.
    print(select_10())  # Список курсів, які певному студенту читає певний викладач.
