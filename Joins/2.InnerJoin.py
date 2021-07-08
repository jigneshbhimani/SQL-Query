# 2.SQL INNER JOIN Keyword:

# INNER JOIN keyword selects records that have matching values in both tables.

# INNER JOIN Syntax:
'''
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
'''
# INNER JOIN keyword selects all rows from both tables as long as there is a match between the columns.



# JOIN Three Tables:
'''
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
'''
# If there are records in the "Orders" table that do not have matches in "Customers", these orders will not be shown!