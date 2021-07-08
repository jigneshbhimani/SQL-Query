# Engine class connects a Pool and Dialect together to provide a source of database connectivity and behavior.
# An object of Engine class is instantiated using the create_engine() function.

# The create_engine() function takes the database as one argument.
# The database is not needed to be defined anywhere.

# create a database:

# 1.Database connectivity:
'''
from sqlalchemy import create_engine, engine
engine = create_engine("sqlite:///student.db",echo=True)
'''

# 2.MySQL database:
'''
engine = create_engine("mysql://user:pwd@localhost/college",echo = True)
'''

# 3.DB-API:
'''
dialect[+driver]://user:password@host/dbname
'''

# 4.PyMySQL driver with MySQL:
'''
mysql+pymysql://<username>:<password>@<host>/<dbname>
'''
