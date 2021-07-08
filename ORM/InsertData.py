# Inserting data into the database:

# The database table is still empty.
# We can insert data into the database using Python objects.
# Because we use the SqlAlchemy ORM we do not have to write a single SQL query.
# We now simply create Python objects that we feed to the ORM. 

import datetime
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from CreateClass import *

# create engine
from sqlalchemy import create_engine
engine = create_engine('sqlite:///student.db', echo=True)

# create a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# create object
user = Student("jigs","Jigs","Patel","IIT")
session.add(user)

user = Student("jack","Jay","Sudra","MIT")
session.add(user)

user = Student("viru","Viral","Sudra","Stanford")
session.add(user)

# commit the record the database
session.commit()
