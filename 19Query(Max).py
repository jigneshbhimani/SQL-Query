# 19.SQL MAX() Query:

# The MAX() function returns the largest value of the selected column.

# MAX() Syntax:
'''
SELECT MAX(column_name)
FROM table_name
WHERE condition;
'''



# Example:
# SQL statement finds the price of the most expensive product
'''
SELECT MAX(Price) AS LargestPrice
FROM Products;
'''