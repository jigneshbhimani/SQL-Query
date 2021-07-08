# 3.SQL COUNT() Query:

# COUNT() function returns the number of rows that matches a specified criterion.

# COUNT() Syntax:
'''
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
'''



# Example:
# SQL statement finds the number of products
# NULL values are not counted.
'''
SELECT COUNT(ProductID)
FROM Products;
'''