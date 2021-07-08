# 1.SQL SELECT Query:

# SELECT query is used to select data from a database.
# The data returned is stored in a result table, called the result-set.

# SELECT syntax:
'''
SELECT column1, column2, ...        # column1, column2, ... are the field names of the table
FROM table_name;    
'''
# select all the fields available in the table
'''
SELECT * FROM table_name;
'''


# SELECT Column Example:
'''
SELECT CustomerName, City FROM Customers
'''
# Where CustomerName and City is column name and Customers is table name.