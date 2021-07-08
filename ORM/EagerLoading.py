# Eager load reduces the number of queries.
# SQLAlchemy offers eager loading functions invoked via query options which give additional instructions to the Query.
# These options determine how to load various attributes via the Query.options() method.

# 1.Subquery Load:
# The orm.subqueryload() option gives a second SELECT statement that fully loads the collections associated with the results just loaded.
# The name “subquery” causes the SELECT statement to be constructed directly via the Query re-used and embedded as a subquery into a SELECT against the related table.
'''
from sqlalchemy.orm import subqueryload
c = session.query(Student).options(subqueryload(Student.teacher)).filter_by(Firstname = 'Jigs').one()
print(c.Username, c.Firstname, c.Lastname, c.School)

for x in c.teacher:
    print("Teacher Id: {}".format(x.Teacher_Id))
'''


# 2.Joined Load:
# The other function is called orm.joinedload().
# This emits a LEFT OUTER JOIN.
# Lead object as well as the related object or collection is loaded in one step.
'''
from sqlalchemy.orm import joinedload
c = session.query(Student).options(joinedload(Student.teacher)).filter_by(Firstname='Jigs').one()
'''
# The OUTER JOIN resulted in two rows, but it gives one instance of Customer back.
# This is because Query applies a “uniquing” strategy, based on object identity, to the returned entities.
# Joined eager loading can be applied without affecting the query results.
# The subqueryload() is more appropriate for loading related collections while joinedload() is better suited for many-to-one relationship.
