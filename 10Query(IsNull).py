# 10.SQL IS NULL Query:

# IS NULL Syntax:
'''
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
'''



# The IS NULL Operator:
# Always use IS NULL to look for NULL values.
# IS NULL operator is used to test for empty values (NULL values).
'''
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NULL;
'''
# SQL lists all customers with a NULL value in the "Address" field: