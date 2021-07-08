# 3.The SAVEPOINT Command:

# It is a point in a transaction when you can roll the transaction back to a certain point without rolling back the entire transaction.

# Syntax:
'''
SAVEPOINT SAVEPOINT_NAME;
'''
# Used only in the creation of SAVEPOINT among all the transaction.
# In genral ROLLBACK is used to undo a group of transaction.
# Syntax for rolling back to Savepoint command:
'''
ROLLBACK TO SAVEPOINT_NAME;
'''
# You can ROLLBACK to any SAVEPOINT at any time to return the appropriate data to its original state.



# Example:
'''
SAVEPOINT S1;                               # First Savepoint created before deletion
//Savepoint created.
DELETE FROM Teacher WHERE AGE = 35;
//deleted
SAVEPOINT S2;                               # Second Savepoint created after deletion
//Savepoint created.
'''
# Delete those records from the table which have age=20 and then ROLLBACK the changes in the database by keeping Savepoints.

# You have decided to ROLLBACK to the SAVEPOINT that you identified as S1 which is before deletion.
# deletion is undone by this statement,
'''
ROLLBACK TO S1;
//Rollback completed.
'''
