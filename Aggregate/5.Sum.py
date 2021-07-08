# 5.SQL SUM() Query:

# SUM() function returns the total sum of a numeric column. 

# SUM() Syntax:
'''
SELECT SUM(column_name)
FROM table_name
WHERE condition;
'''



# Example:
# SQL statement finds the sum of the "Quantity" fields in the "OrderDetails" table
# NULL values are ignored.
'''
SELECT SUM(Quantity)
FROM OrderDetails;
'''