from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    address = Column(String(150), nullable=True)
    phone = Column('cell_phone', String(150), nullable=True)
    statr_work = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())

    subjects = relationship('Subject', back_populates='teacher')
    students = relationship('Student', secondary='techers_to_students', back_populates="teachers")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    address = Column(String(150), nullable=True)
    phone = Column('cell_phone', String(150), nullable=True)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')
    teachers = relationship('Teacher', secondary='techers_to_students', back_populates="students")


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship('Student', back_populates='group')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    date = Column(DateTime, default=datetime.now())
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')


class TeacherStudent(Base):
    __tablename__ = "techers_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
