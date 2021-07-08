# 7.SQL OR Query:

# WHERE clause can be combined with OR operator.
# OR operator is used to filter records based on more than one condition:
# The OR operator displays a record if any of the conditions separated by OR is TRUE.

# OR Syntax:
'''
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
'''



# OR Example:
'''
SELECT * FROM Customers
WHERE City='Baroda' OR City='Rajkot';
'''