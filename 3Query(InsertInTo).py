# 3.SQL INSERT INTO Query:

# INSERT INTO query is used to insert new records in a table.

# INSERT INTO Syntax:

# To write the INSERT INTO query in two ways:
# a...Specify both the column names and the values to be inserted
'''
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
'''
# b...If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query.
'''
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
'''


# Insert Data Only in Specified Columns:
'''
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
'''
# where CustomerName, City, and Country columns name and Customers table name