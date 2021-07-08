# 10.SQL IS NOT NULL Query:

# IS NOT NULL Syntax:
'''
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
'''



# The IS NOT NULL Operator:
# IS NOT NULL operator is used to test for non-empty values (NOT NULL values).
'''
SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address IS NOT NULL;
'''
# SQL lists all customers with a value in the "Address" field