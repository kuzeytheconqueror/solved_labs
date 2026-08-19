# Query Gate

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** SQL, MySQL, Misconfiguration

## Database
Database is a system for storing, managing and accessing data in an
organized and efficient way.

Databases provide fast and secure access to data by storing data in an
organized way. Data is kept in the form of tables, columns and rows. Thanks
to this method, we can access data quickly and securely.

## Database Functions
**Data Storage**: Stores data in a secure and organized manner.
**Data Querying**: Provides fast and efficient access to data.
**Data updating**: Provides the capability to update the data.
**Security and Access Control**: Prevents unauthorized access and ensures data security.

## SQL
SQL (Structured Query Language) is a language used to manage and query
data in databases. These operations include inserting, updating, deleting and
retrieving data from the database.

SQL is a way of interacting with the database. Learning the SQL language
and being able to write SQL queries is important for understanding and using
databases.

## Database Types
**Relational Databases (SQL)**: It stores data in tables. Each table consists of
columns and rows. Some common SQL databases: MySQL, PostgreSQL.

**Documented Based Databases (NoSQL)**: It stores data in document form using
structures such as JSON, XML. Some common NoSQL databases: MongoDB,
CouchDB.

**Key-Value Databases**: Stores data using simple key-value pairs. Provides
fast access to data. Some common key-value databases: Redis, DynamoDB.

## MySQL
MySQL is a popular relational database management system (RDBMS)
widely used worldwide. It is known for being open source, having a large
community of users and developers, and being available on various
operating systems.

MySQL uses Structured Query Language (SQL) for data manipulation and
querying. SQL, also used in MySQL, is a standard language for interacting
with databases.

Below are examples of SQL commands used in MySQL for various database
and table operations.

## Select
Used to select and display specific data from the database.

```sql
SELECT name, surname, age FROM users;
```

This query selects the "name", "surname", "age" columns from the "users"
table and retrieves the data in them.

## Insert
Used to insert new data into the table.

```sql
INSERT INTO users (name, surname, age) VALUES (‘Lynn’,’Spence‘, 37);
```

This query creates a new row in the "users" table and adds "Lynn", "Spence"
and 37 to the "name", "surname" and "age" columns respectively.

## Update
It is used to update data in the table.

```sql
UPDATE users SET age = 34 WHERE name = ’Lynn’;
```

This query updates the “age” information to 34 for the records in the “users”
table where the “name” column contains “Lynn”.

## Delete
It is used to delete data in the table.

```sql
DELETE FROM users WHERE age > 60;
```

This query deletes the records in the "users" table if the data in the "age"
column is greater than 60.

## List Databases
A SQL server can have many different databases. We can run the following
command to list these databases.

```sql
SHOW DATABASES;
```

## Select Databases
We can run the following command to select the database we will be working on.

```sql
USE <database-name>;
```

## Delete Databases
To delete a database we can execute the following command.

```sql
DROP DATABASE <database-name>;
```

### List Tables
There can be many different tables in a database. We can run the following
command to list the tables in the selected database.

```sql
SHOW TABLES;
```

### Delete Tables
To delete a table we can execute the following command.

```sql
DROP TABLE <table-name>;
```

### Display Table Information
To display the columns and data types of a table we can execute the
following command.

```sql
DESCRIBE <table-name>;
```

## Information Gathering
Let's gather information by running a port scan on our target machine.

## Task 1, Task 2

```bash
nmap <ip>
```

## System Access
Let's try connecting to the target MySQL server.

## Task 3, Task 4
The tasks asks for the most authorized user, so root should come directly to mind. We will try to connect the target MySQL server with this username

The command string we will use to connect to MySQL is as follows.

```bash
mysql -u root -h <target>
```

- `-u` — Used to specify which user to connect as when connecting to the
  target machine.
- `-h` — Parameter used to specify the IP address or hostname of the target
  machine.
- `-P` — Parameter used to specify the port number.

Note: If MySQL uses port 3306 by default, we do not need to specify a port
number when connecting.

Yes, as we expected, we were able to access the MySQL command line by
connecting to our target machine with the root user.

Normally, when connecting to MySQL, you connect with username and
password. Unless this configuration was done intentionally, we can say that
there is a misconfiguration on the target machine.

## Task 5
To see how many databases there are, let's run the `SHOW DATABASES;`
command from the MySQL command line we are connected to.

```sql
SHOW DATABASES;
```

## Task 6 and 7
To view the tables in the `detective_inspector` database that attracted our
attention, we first select this database using the `USE` command. Then we will
run the `SHOW TABLES;` command to list the tables.

```sql
USE detective_inspector;
```

```sql
SHOW TABLES;
```

We discovered that there is a table named `hacker_list` in the database we
are targeting.

## Task 8

Let's look at the data in the table to identify the white hat hacker.
