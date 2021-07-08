# These are the operators which build on relationship.
# 1.__eq__()
# 2.__ne__()
# 3.contains()
# 4.any()
# 5.has()

# 1.__eq__():
# many-to-one “equals” comparison
# To compare two objects by their values.
'''s = session.query(Student).filter(Teacher.Tec_Firstname.__eq__('Jigs'))'''

# 2.__ne__():
# many-to-one “not equals” comparison
# Return with True or False that values are not equal.
'''s = session.query(Student).filter(Teacher.Student_Id.__ne__(2))'''

# 3.contains():
# Used for one-to-many collections
# Only accepts one Model object instead of a list of objects.
'''s = session.query(Teacher).filter(Teacher.Techer_No.contains([3,4,5]))'''

# 4.any():
# Used for collections
'''s = session.query(Student).filter(Student.teacher.any(Teacher.Teacher_no == 11))'''

# 5.has():
# Used for scalar references
'''s = session.query(Teacher).filter(Teacher.student.has(Firstname = 'Jay'))'''