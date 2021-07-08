# 4.SQL UPDATE Query:

# UPDATE query is used to modify the existing records in a table.

# UPDATE Syntax:
'''
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
'''



# UPDATE Table:
# SQL query updates the first customer(CustomerID = 1) with a new contact person and a new city.
'''
UPDATE Customers
SET ContactName = 'Jignesh', City= 'Rajkot'
WHERE CustomerID = 1;
'''



# UPDATE Multiple Records:
# It is the WHERE clause that determines how many records will be updated.
'''
UPDATE Customers
SET ContactName='John'
WHERE Country='India';
'''
# SQL query will update the ContactName to "John" for all records where country is "India"

