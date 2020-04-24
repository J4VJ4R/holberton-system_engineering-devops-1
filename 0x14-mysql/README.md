# MySQL replication challenge
This repository contains information about bellow applied concepts:

## Concepts
- Database administration
- Web stack debugging
- mysqldump
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Requirements
- Linux Ubuntu 16.04 LTS
- MySQL distribution must be 5.7.x

## Context
![replication](https://github.com/gogomillan/holberton-system_engineering-devops/blob/master/0x14-mysql/assets/db_replication.png)

## Challenges

###  0. Install MySQL
First things first, lets get MySQL installed on both servers.

**Example**
```bash wrap
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

###  1. Let us in!
In order for us to verify that the servers are properly configured, we need you to
create a user and password for both MySQL databases which will allow the checker access to them.

**Example**
```bash wrap
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

###  2. If only you could see what I've seen with your eyes

Base schema in order to set up replication. One table and one row in the
primary MySQL server.

**Example**
```bash wrap
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

###  3. Quite an experience to live in fear, isn't it?

Before you get started with the primary-replica synchronization, it is needed
to create a new user for the replica server.
