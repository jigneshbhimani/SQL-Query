# 6.SQL AND Query:

# WHERE clause can be combined with AND operator.
# AND operator is used to filter records based on more than one condition:
# The AND operator displays a record if all the conditions separated by AND are TRUE.

# AND Syntax:
'''
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
'''



# AND Example:
'''
SELECT * FROM Customers
WHERE Country='India' AND City='Rajkot';
'''