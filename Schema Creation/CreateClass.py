# ORM with SqlAlchemy:

# An object relational mapper maps a relational database system to objects.
# The ORM is independent of which relational database system is used.
# From within Python, you can talk to objects and the ORM will map it to the database.

# communicate with the database using the ORM and only use Python objects and classes.
'''
Python Classes <-> ORM <-> SQL Database
'''


# Creating a class to feed the ORM:

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.engine import base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# Create engine
engine = create_engine('sqlite:///student.db', echo=True)       

# Base class creating function called declarative base 
# Create Base class
Base = declarative_base()

class Student(Base):
    
    __tablename__ = "student"

    Id = Column(Integer,primary_key=True)
    Username = Column(String)
    Firstname = Column(String)
    Lastname = Column(String)
    School = Column(String)

    def __init__(self, Username, Firstname, Lastname, School):
        self.Username = Username
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.School = School

# create tables
Base.metadata.create_all(engine)