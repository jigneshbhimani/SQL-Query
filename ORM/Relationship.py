# 1.One To Many
'''
It refers to parent with the help of a foreign key on the child table.
relationship() is then specified on the parent, as referencing a collection of items represented by the child.
The relationship.back_populates parameter is used to establish a bidirectional relationship in one-to-many, where the “reverse” side is a many to one.
'''

# 2.Many To One
'''
It places a foreign key in the parent table to refer to the child.
relationship() is declared on the parent, where a new scalar-holding attribute will be created.
The relationship.back_populates parameter is used for Bidirectionalbehaviour.
'''

# 3.One To One
'''
It is essentially a bidirectional relationship in nature.
The uselist flag indicates the placement of a scalar attribute instead of a collection on the “many” side of the relationship.
To convert one-to-many into one-to-one type of relation, set uselist parameter to false.
'''

# 4.Many To Many
'''
It is established by adding an association table related to two classes by defining attributes with their foreign keys.
It is indicated by the secondary argument to relationship().
The relationship.back_populates parameter for each relationship() establishes a bidirectional relationship.
Both sides of the relationship contain a collection.
'''


# Example:
'''
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

engine = create_engine('sqlite:///student.db', echo = True)

class Student(Base):
    __tablename__ = 'student'
    Id = Column(Integer,primary_key=True)
    Username = Column(String)
    Firstname = Column(String)
    Lastname = Column(String)
    School = Column(String)

class Teacher(Base):
    __tablename__ = 'teacher'
    Tec_Id = Column(Integer,primary_key=True)
    Student_Id = Column(Integer,ForiegnKey('student.Id'))
    Tec_Username = Column(String)
    Tec_Firstname = Column(String)
    abc = relationship("Student",back_populates="teacher")

Student.teacher = relationship("Teacher", order_by=Teacher.Tec_Id, back_populates="abc")
Base.metadat.create_all(engine)
'''