-- Script that prepares a MySQL server for the project:
-- Creates the user holberton_user.
DROP USER IF EXISTS holberton_user@localhost;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
