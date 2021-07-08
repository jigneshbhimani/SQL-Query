# 4.The RELEASE SAVEPOINT Command:

# Used to remove a SAVEPOINT that you have created.

# Syntax:
'''
RELEASE SAVEPOINT SAVEPOINT_NAME;
'''
# Once a SAVEPOINT has been released, you can no longer use the ROLLBACK command to undo transaction performed since the last SAVEPOINT.