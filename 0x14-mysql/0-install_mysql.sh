#!/usr/bin/env bash
# Bash script that install MySQL on the server
sudo apt-get update -y
sudo apt-get install mysql-server-5.7 -y
mysql --version
