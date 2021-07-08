# 27.SQL Aliases:

# SQL aliases are used to give a table, or a column in a table, a temporary name.
# Aliases are often used to make column names more readable.
# An alias only exists for the duration of that query.
# An alias is created with the AS keyword.

# Alias Column Syntax:
'''
SELECT column_name AS alias_name
FROM table_name;
'''

# Alias Table Syntax:
'''
SELECT column_name(s)
FROM table_name AS alias_name;
'''



# Alias for Columns Examples:
# SQL statement creates two aliases, one for the CustomerID column and one for the CustomerName column
'''
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
'''

# SQL statement creates two aliases, one for the CustomerName column and one for the ContactName column.
# It requires double quotation marks or square brackets if the alias name contains spaces.
'''
SELECT CustomerName AS Customer, ContactName AS [Contact Person]
FROM Customers;
'''

# SQL statement creates an alias named "Address" that combine four columns(Address,PostalCode,City and Country)
'''
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;
'''



# Alias for Tables Example:
# SQL statement selects all the orders from the customer with CustomerID=4 (Around the Horn).
# We use the "Customers" and "Orders" tables, and give them the table aliases of "c" and "o" respectively.
'''
SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
'''

# SQL statement is the same as above, but without aliases
'''
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;
'''

# Aliases can be useful when:

# 1.There are more than one table involved in a query
# 2.Functions are used in the query
# 3.Column names are big or not very readable
# 4.Two or more columns are combined together