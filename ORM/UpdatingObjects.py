# Updating Objects:

# 1.Fetch an object from the table whose primary key identifier, in our Customers table with ID=2 using get()
'''x = session.query(Student).get(2)'''

# Display contents of the selected object
'''
print("Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''
# Output:
'''Username:jack Firstname:Jay Lastname:Sudra School:MIT'''



# 2.Update the Lastname field by assigning new value:
# Change the field x.Username/Firstname/Lastname/School
'''
x.Lastname = 'Jadav'
session.commit()
'''



# 3.Fetch object corresponding to first row in the table by using first() method.
'''x = session.query(Student).first()'''

# Display contents of the selected object
'''
print("Username:",x.Username, "Firstname:",x.Firstname, "Lastname:",x.Lastname, "School:",x.School)
'''
# Output:
'''Username:jigs Firstname:Jigs Lastname:Patel School:IIT'''



# 4.For bulk updates, we shall use update() method of the Query object.
# ‘Mr.’ to name in each row (except ID = 2). The corresponding update() statement.
'''
session.query(Student).filter(Student.Id != 2)
update({Student.Firstname:"Mr."+Student.Firstname, synchronize_session=False})
'''