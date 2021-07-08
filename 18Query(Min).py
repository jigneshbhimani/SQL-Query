# 18.SQL MIN() Query:

# The MIN() function returns the smallest value of the selected column.

# MIN() Syntax:
'''
SELECT MIN(column_name)
FROM table_name
WHERE condition;
'''



# Example:
# SQL statement finds the price of the cheapest product
'''
SELECT MIN(Price) AS SmallestPrice
FROM Products;
'''