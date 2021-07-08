# 9.Combining AND, OR and NOT:


# Example:
'''
SELECT * FROM Customers
WHERE Country='India' AND (City='Baroda' OR City='Rajkot');
'''

# Example:
'''
SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';
'''