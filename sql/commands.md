# SQL Commands

### Log into MySQL 
```
mysql -u user -p
```

### Creating a MySQL User
```
CREATE USER 'user'@'host';
```

### Granting specific privileges to a user on an object
```
GRANT privileges_name ON object TO user;
```

### Set password for the current user
```
SET PASSWORD='password'
```

### Create a new database
```
CREATE DATABASE database_name;
```

### Access a specific database
```
USE database_name;
```

### Delete a specific database
```
DROP DATABASE database_name;
```

### List out all databases on the MySQL Server
```
SHOW DATABASES;
```

### List out all MySQL Users
```
SELECT user FROM mysql.user;
```
