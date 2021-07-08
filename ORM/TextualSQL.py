# Literal strings can be used flexibly with Query object by specifying their use with the text() construct.
# Most applicable methods accept it. For example, filter() and order_by().

# filter() method translates the string “id<3” to the WHERE id<3
'''
from sqlalchemy import text
for stud in session.query(Student).filter(text("id<3")):
   print(stud.Firstname)
'''

# To specify bind parameters with string-based SQL, use a colon,and to specify the values, use the params() method.
'''
stud = session.query(Student).filter(text("id = :value")).params(value = 1).one()
'''

# To use an entirely string-based statement, a text() construct representing a complete statement can be passed to from_statement().
'''
session.query(Customers).from_statement(text("SELECT * FROM customers")).all()
'''

# The text() construct allows us to link its textual SQL to Core or ORM-mapped column expressions positionally.
# We can achieve this by passing column expressions as positional arguments to the TextClause.columns() method.
'''
stmt = text("SELECT id, Username, Firstname, Lastname, School FROM student")
stmt = stmt.columns(Student.Id, Student.Firstname)
session.query(Student.Id, Student.Firstname).from_statement(stmt).all()
'''
