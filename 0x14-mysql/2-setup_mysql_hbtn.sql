-- Script that prepares a MySQL server for the project:
-- Creates the db tyrell_corp.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
-- Creates the table nexus6
CREATE TABLE nexus6
(
  id INT(20),
  name VARCHAR(40)
);
-- Insert data on table nexus 6
INSERT INTO nexus6(id, name)
VALUES(1, "Leon");
COMMIT;
-- Creates the user holberton_user.
DROP USER IF EXISTS holberton_user@localhost;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
