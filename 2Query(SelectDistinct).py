# 2.SQL SELECT DISTINCT Query:

# SELECT DISTINCT query is used to return only distinct (different) values.
# Column often contains many duplicate values; and you only want to list the different(distinct) values.

# SELECT DISTINCT Syntax:
'''
SELECT DISTINCT column1, column2, ...
FROM table_name;
'''

# SELECT DISTINCT Examples:
'''
SELECT DISTINCT Country FROM Customers;
'''
# where Country is column name and Customers table name



# lists the number of different(distinct) customer countries:
'''
SELECT COUNT(DISTINCT Country) FROM Customers;
'''
