# 14.SQL LEFT JOIN Keyword:

# LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table (table2).
# The result is 0 records from the right side, if there is no match.
# Some databases LEFT JOIN is called LEFT OUTER JOIN.

# LEFT JOIN Syntax:
'''
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
'''



# SQL LEFT JOIN Example:
'''
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;
'''
# LEFT JOIN keyword returns all records from the left table (Customers), even if there are no matches in the right table (Orders).