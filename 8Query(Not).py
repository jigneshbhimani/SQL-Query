# 8.SQL NOT Query:

# WHERE clause can be combined with NOT operator.
# NOT operator displays a record if the condition is NOT TRUE.

# NOT Syntax:
'''
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
'''



# NOT Example:
'''
SELECT * FROM Customers
WHERE NOT Country='India';
'''