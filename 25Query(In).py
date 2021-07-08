# 25.SQL IN Operator:

# The IN operator allows you to specify multiple values in a WHERE clause.
# The IN operator is a shorthand for multiple OR conditions.

# IN Syntax:
'''
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
'''
# or
'''
SELECT column_name(s)
FROM table_name
WHERE column_name IN (SELECT STATEMENT);
'''



# IN Operator Examples:
# SQL statement selects all customers that are located in "India", "USA" or "Turkey"
'''
SELECT * FROM Customers
WHERE Country IN ('India', 'USA', 'Turkey');
'''

# SQL statement selects all customers that are NOT located in "India", "USA" or "Turkey"
'''
SELECT * FROM Customers
WHERE Country BOT IN ('India', 'USA', 'Turkey');
'''

# SQL statement selects all customers that are from the same countries as the suppliers
'''
SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);
'''