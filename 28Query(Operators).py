# 28.SQL Operators:

# SQL Arithmetic Operators:

# Add(+):
'''
SELECT 5 + 9;
'''

# Subtract(-):
'''
SELECT 5 - 9;
'''

# Multiply(*):
'''
SELECT 5 * 9;
'''

# Divide(/):
'''
SELECT 8 / 4;
'''

# Modulo(%):
'''
SELECT 45 - 5;
'''

# SOME:
# TRUE if any of the subquery values meet the condition
'''
SELECT * FROM Products
WHERE Price > SOME (SELECT Price FROM Products WHERE Price > 20);
'''