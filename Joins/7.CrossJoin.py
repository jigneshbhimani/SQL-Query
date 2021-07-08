# 7.SQL CROSS or CARTESIAN Join:

# It returns the Cartesian product of the sets of records from two or more joined tables.
# Thus, it equates to an inner join where the join-condition always evaluates to either True or where the join-condition is absent from the statement.

# Syntax:
'''
SELECT table1.column1, table2.column2...
FROM  table1, table2 [, table3 ]
'''



# Examples:
# Consider two tables one is CUSTOMERS and another one is ORDERS.
# let us join these two tables using CARTESIAN JOIN.
'''
SELECT Id, Name, Amount, Date FROM CUSTOMERS, ORDERS;
'''