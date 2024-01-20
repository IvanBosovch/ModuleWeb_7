from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres', echo=True)

DBSession = sessionmaker(bind=engine)
session = DBSession()

class Base(DeclarativeBase):
    pass


class Groups(Base):
    __tablename__ = 'groups'
    groups_id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String(50))


class Students(Base):
    __tablename__ = 'students'
    students_id: Mapped[int] = mapped_column(primary_key=True)
    students_name: Mapped[str] = mapped_column(String(50))
    groups_id: Mapped[int] = mapped_column(ForeignKey('groups.groups_id'))
    group: Mapped['Groups'] = relationship('Groups', backref='students')
    #garde: Mapped['Grades'] = relationship(back_populates= 'students')


class Teachers(Base):
    __tablename__ = 'teachers'
    teachers_id: Mapped[int] = mapped_column(primary_key=True)
    teachers_name: Mapped[str] = mapped_column(String(50))
    #discipline: Mapped['Disciplines'] = relationship(backref='teachers')


class Disciplines(Base):
    __tablename__ = 'disciplines'
    disciplines_id: Mapped[int] = mapped_column(primary_key=True)
    disciplines_name: Mapped[str] = mapped_column(String(50), unique=True)
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.teachers_id'))
    teacher: Mapped['Teachers'] = relationship('Teachers', backref='disciplines')


class Grades(Base):
    __tablename__ = 'grades'
    grades_id: Mapped[int] = mapped_column(primary_key= True)
    grades: Mapped[int]
    date_grade: Mapped[datetime]
    students_id: Mapped[int] = mapped_column(ForeignKey('students.students_id'))
    student: Mapped['Students'] = relationship('Students', backref='grades')
    disciplines_id: Mapped[int] = mapped_column(ForeignKey('disciplines.disciplines_id'))
    disciplines: Mapped['Disciplines'] = relationship('Disciplines', backref='grades')


if __name__ == '__main__':
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine)    
    Base.metadata.bind = engine               

