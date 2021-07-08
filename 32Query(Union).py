# 32.SQL UNION Operator:

# Used to combine the result-set of two or more SELECT statements.
# 1.Every SELECT statement within UNION must have the same number of columns
# 2.The columns must also have similar data types
# 3.The columns in every SELECT statement must also be in the same order

# UNION Syntax:
# UNION operator selects only distinct values by default.
'''
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
'''

# SQL UNION Example:
# SQL query returns the cities (only distinct values) from both the "Customers" and the "Suppliers" table
'''
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
'''




# UNION ALL Syntax:
# To allow duplicate values, use UNION ALL.
'''
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
'''

# SQL UNION ALL Example:
# SQL statement returns the cities (duplicate values also) from both the "Customers" and the "Suppliers" table
'''
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
'''

