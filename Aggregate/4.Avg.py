# 4.SQL AVG() Query:

# AVG() function returns the average value of a numeric column. 

# AVG() Syntax:
'''
SELECT AVG(column_name)
FROM table_name
WHERE condition;
'''



# Example:
# SQL statement finds the average price of all products
# NULL values are ignored.
'''
SELECT AVG(Price)
FROM Products;
'''