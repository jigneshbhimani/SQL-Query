# These are Filter Operators.
# 1.Equals
# 2.Not Equals
# 3.Like
# 4.In
# 5.And
# 6.Or

# 1.Equals:
# Used is == and it applies the criteria to check equality.
# Print field that Id given in below statement
'''
result = session.query(Student).filter(Student.Id == 2)
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''

# 2.Not Equals:
# Used for not equals is != and it provides not equals criteria.
# Not Print field that Id given in below statement
'''
result = session.query(Student).filter(Student.Id != 2)
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''

# 3.Like:
# Produces the LIKE criteria for WHERE clause in the SELECT expression.
# Print that field where Firstname start with 'J'.
'''
result = session.query(Student).filter(Student.Firstname.Like('J%'))
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''

# 4.In:
# Checks whether the column value belongs to a collection of items in a list.
# Print field that Id[1,3] given in statement
'''
result = session.query(Student).filter(Student.Id.in_([1,3]))
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''

# 5.And:
# Putting multiple commas separated criteria in the filter or using and_() method
# Print field that Id>1 and Firstname starts with 'J'
'''
result = session.query(Student).filter(Student.Id>1, Student.Firstname.Like('J%'))
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''

# 6.Or:
# Print both field that Id>1 and Firstname starts with 'J'
'''
result = session.query(Student).filter(or_(Student.Id>1, Student.Firstname.Like('J%')))
for x in result:
    print("Id:",x.Id, "Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''