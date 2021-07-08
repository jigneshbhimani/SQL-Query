# Query the data

# We can query all items of the table using the code below.
# Python will see every record as a unique object as defined by the Students class.

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from CreateClass import *

# create engine
engine = create_engine('sqlite:///student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# create object
# for student in session.query(Student).order_by(Student.Id):
#     print(student.Firstname, student.Lastname)


'''             OR-OR-OR-OR-OR-OR               '''


# To select a single object use the filter() method.
# Select objects 
for student in session.query(Student).filter(Student.Firstname == 'Jigs'):
    print(student.Firstname, student.Lastname)


# if you do not want the ORM the output any of the SQL queries change the create_engine statement:
'''engine = create_engine('sqlite:///student.db', echo=False)'''
