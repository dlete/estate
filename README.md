### Summary
- Discover part numbers in SNMP enabled machines
- Have a table with the theoretical estate
- Reconcile discovered and theoretical estate


###### Markdown
https://help.github.com/articles/github-flavored-markdown
https://help.github.com/articles/markdown-basics
https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown

###### nginx
- for php: https://www.digitalocean.com/community/articles/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04

###### Python
- version 2.7
- conventions in https://www.python.org/dev/peps/pep-0008

###### SQL
- connector info: https://docs.djangoproject.com/en/dev/ref/databases/#mysql-db-api-drivers
- connector installed: pip install MySQL-python
- MySQL 5.6
- sudo mysql_secure_installation 
-   CREATE DATABASE <db_name> CHARACTER SET utf8;
    CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';
    GRANT ALL PRIVILEGES ON <db_name>.* TO '<user>'@'localhost';
    FLUSH PRIVILEGES;

###### virtualenv
mkvirtualenv -p /usr/bin/python3 <environment>
