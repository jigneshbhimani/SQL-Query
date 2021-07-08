# Query object can be subjected to certain criteria by using filter() method.
'''session.query(class).filter(criteria)'''

# Example:
# SELECT query on Customers table is filtered by a condition, (ID>2) 
'''result = session.query(Student).filter(Student.Id>2)'''

'''
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///student.db', echo = True)

class Student(Base):
    __tablename__ = 'student'
    Id = Column(Integer,primary_key=True)
    Username = Column(String)
    Firstname = Column(String)
    Lastname = Column(String)
    School = Column(String)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Student).filter(Student.Id>2)

for row in result:
   print ("Id:", row.Id, "Username: ",row.Username, "Firstname:",row.Firstname, "Lastname:",row.Lastname, "School:",row.School)
'''