# 23.SQL WHERE Clause:

# WHERE clause is used to filter records.
# Used to extract only those records that fulfill a specified condition.
# WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc...

# WHERE Syntax:
'''
SELECT column1, column2, ...
FROM table_name
WHERE condition;
'''



# WHERE Clause Example:
# SQL statement selects all the customers from the country "India", in the "Customers" table
'''
SELECT * FROM Customers
WHERE Country='India';
'''



# Text Fields vs. Numeric Fields:
# SQL requires single quotes around text values (most database systems will also allow double quotes).
# However, numeric fields should not be enclosed in quotes
# Example:
'''
SELECT * FROM Customers
WHERE CustomerID=1;
'''



# Operators in The WHERE Clause:

# a...Equal(=):
'''
SELECT * FROM Products
WHERE Price = 18;
'''

# b...Greater Than(>):
'''
SELECT * FROM Products
WHERE Price > 30;
'''

# c...Less Than(<):
'''
SELECT * FROM Products
WHERE Price < 30;
'''

# d...Greater than or Equal to(>=):
'''
SELECT * FROM Products
WHERE Price >= 30;
'''

# e...Less than or Equal to(<=):
'''
SELECT * FROM Products
WHERE Price <= 30;
'''

# f...Not Equal(!= or <>):
'''
SELECT * FROM Products
WHERE Price <> 18;
'''