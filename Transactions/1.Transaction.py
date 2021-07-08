# 1.What is a transaction?
# A transaction is a set of operations performed so all operations are guaranteed to succeed or fail as one unit.
# It is a unit of work that is performed against a database.


# 2.Properties of Transaction.
# Transaction following ACID properties.
# -> Atomocity : ensures that all operations within the work unit are completed successfully.
#                Otherwise, the transaction is aborted at the point of failure and all the previous operations are rolled back to their former state.
# -> Consistency : ensures that the database properly changes states upon a successfully committed transaction.
# -> Isolation : enables transactions to operate independently of and transparent to each other.
# -> Durability : ensures that the result or effect of a committed transaction persists in case of a system failure.


# 3.When to use transaction?
# You should use transactions when several operations must succeed or fail as a unit.
# -> In batch processing, where multiple rows must be inserted, updated or deleted as a single unit.
# -> Whenever a change to one table reqiures that other tables be kept consistent.
# -> When modifying data in two or more database concurrently.
# -> In distributed transactions, where data is manipulated in databases on various servers.


# 4.Concurrency:
# When you use transaction, you put locks on data that is pending for permanent change to the database.
# No other operations can take place on locked data until the acquired lock is released.
# You could lock anything from a single row up to the entire database.
# This is called concurrency, which means how the database handles multiple updates at one time.


# 5.Transaction Control:
# These are the commands are used to control transactions.
# -> COMMIT - to save the changes.
# -> ROLLBACK - to roll back the changes.
# -> SAVEPOINT - creates points within the groups of transactions in which to ROLLBACK.
# -> SET TRANSACTION - places a name on a transaction.