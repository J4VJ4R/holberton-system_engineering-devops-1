-- Script that prepares a MySQL server for the project: Run in replica server. Rus as root
-- Set the right DB config
CHANGE MASTER TO MASTER_HOST='35.196.121.157',MASTER_USER='replica_user', MASTER_PASSWORD='replica_user', MASTER_LOG_FILE='mysql-bin.000031', MASTER_LOG_POS=154;
