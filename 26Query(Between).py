# 26.SQL BETWEEN Operator:

# The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.
# The BETWEEN operator is inclusive: begin and end values are included. 

# BETWEEN Syntax:
'''
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
'''



# BETWEEN Example:
# SQL query selects all products with a price between 5 and 9.
'''
SELECT * FROM Products
WHERE Price BETWEEN 5 AND 9;
'''

# NOT BETWEEN Example:
'''
SELECT * FROM Products
WHERE Price NOT BETWEEN 5 AND 9;
'''

# BETWEEN with IN Example:
# SQL statement selects all products with a price between 5 and 9. In addition; do not show products with a CategoryID of 1,2, or 3
'''
SELECT * FROM Products
WHERE Price BETWEEN 5 AND 9
AND CategoryID NOT IN (1,2,3);
'''

# BETWEEN Text Values Example:
# SQL statement selects all products with a ProductName between Pen and Bike
'''
SELECT * FROM Products
WHERE ProductName BETWEEN 'Pen' AND 'Bike'
ORDER BY ProductName;
'''

# NOT BETWEEN Text Values Example:
# SQL statement selects all products with a ProductName not between Pen and Bike
'''
SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Pen' AND 'Bike'
ORDER BY ProductName;
'''

# BETWEEN Dates Example:
# SQL statement selects all orders with an OrderDate between '24-Nov-1998' and '24-Nov-2000'
'''
SELECT * FROM Orders
WHERE OrderDate BETWEEN #24/11/1998# AND #24/11/2000#;
'''
# or
'''
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1998-24-11' AND '2000-24-11';
'''