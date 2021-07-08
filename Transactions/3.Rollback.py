# 2.The ROLLBACK Command:

# Used to undo transactions that have not already been saved to the database.
# Used to undo transactions since the last COMMIT or ROLLBACK command was issued.

# Syntax:
'''
ROLLBACK;
'''



# Example:
'''
DELETE FROM Teacher WHERE AGE = 35;
ROLLBACK;
'''
# Delete those records from the table which have age=35 and then ROLLBACK the changes in the database.