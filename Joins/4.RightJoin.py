# 4.SQL RIGHT JOIN Keyword:

# RIGHT JOIN keyword returns all records from the right table(table2), and the matching records from the left table(table1).
# The result is 0 records from the left side, if there is no match.
# some databases RIGHT JOIN is called RIGHT OUTER JOIN.

# RIGHT JOIN Syntax:
'''
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
'''



# SQL RIGHT OUTER JOIN Example:
# SQL statement will return all employees, and any orders they might have placed
'''
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;
'''
# RIGHT JOIN keyword returns all records from the right table(Employees), even if there are no matches in the left table(Orders).