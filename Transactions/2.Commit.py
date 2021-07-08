# 1.The COMMIT Command: 

# Used to save changes invoked by a transaction to the database.
# Saves all the transactions to the database since the last COMMIT or ROLLBACK command.

# Syntax:
'''
COMMIT;
'''



# Example:
'''
DELETE FROM Teacher WHERE AGE = 35;
COMMIT;
'''
# Delete those records from the table which have age=35 and then COMMIT the changes in the database.