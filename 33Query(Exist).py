# 33.SQL EXIST Operator:

# Used to test for the existence of any record in a subquery.
# Returns TRUE if the subquery returns one or more records.

# EXISTS Syntax:
'''
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
'''



# SQL EXISTS Examples:
# SQL query returns TRUE and lists the suppliers with a product price less than 16.
'''
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 16);
'''

# SQL statement returns TRUE and lists the suppliers with a product price equal to 16.
'''
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price = 16);
'''