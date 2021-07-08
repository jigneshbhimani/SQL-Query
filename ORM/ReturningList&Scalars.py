# There are a number of methods of Query object that immediately issue SQL and return a value containing loaded database results.

# all():
# It returns a list.
'''session.query(Student).all()'''

# one():
# fully fetches all rows, and if there is not exactly one object identity or composite row present in the result, it raises an error.
'''session.query(Student).one()'''



# Scalar():
# It invokes the one() method, and upon success returns the first column of the row
'''session.query(Student).filter(Stuudent.Id == 2).scalar()'''