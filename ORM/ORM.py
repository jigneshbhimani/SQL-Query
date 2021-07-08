# An object-relational mapper(ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

# Why are ORMs useful?
# Provide a high-level abstraction upon a relational database.
# That allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.


# 1.MetaData.create_all():
# Each Table object is a member of larger collection known as MetaData.
# This object is available using the .metadata attribute of declarative base class.
# The MetaData.create_all() method is, passing in our Engine as a source of database connectivity.
'''
Base.metadata.create_all(engine)
'''

# 2.sessionmaker():
# A session object is the handle to database.
# Session class is defined using sessionmaker() – a configurable session factory method which is bound to the engine object created earlier.
'''
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
'''

# 3.session = Session():
# The session object is then set up using its default constructor
'''
session = Session()
'''

# 4. session.___():
'''
begin(): begins a transaction on this session
add(): places an object in the session. Its state is persisted in the database on next flush operation
add_all(): adds a collection of objects to the session
commit(): flushes all items and any transaction in progress
delete(): marks a transaction as deleted
execute(): executes a SQL expression
flush(): flushes all object changes to the database
expire(): marks attributes of an instance as out of date
invalidate(): closes the session using connection invalidation
rollback(): rolls back the current transaction in progress
close(): Closes current session by clearing all items and ending any transaction in progress
'''

# 5.add_all():
# To add multiple records, we can use add_all() method of the session class.
'''
session.add_all([
   Student(Username = 'jigs', Firstname = 'Jigs', Lastname = 'Patel', School = 'IIT'), 
   Student(Username = 'jack', Firstname = 'Jay', Lastname = 'Sudra', School = 'MIT'), 
   Student(Username = 'viru', Firstname = 'Viru', Lastname = 'Sudra', School = 'Stanford')]
)
session.commit()
'''