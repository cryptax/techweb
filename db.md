# Databases

## MySQL

### Interactive

Example: 

```
mysql --user=root --password='...'
mysql> show databases;
mysql> show tables from owncloud;
mysql> show columns from oc_contacts_addressbooks from owncloud;

```

Create an account:

`create user 'myusername'@'localhost' identified by 'mypassword';`


### Backup / Restore

```
mysqldump -u root -p --all-databases > fruitic.sql
mysqldump --defaults-extra-file="/etc/mysql/backup.cnf" --all-databases -u root --add-drop-database > databases.sql
```

with :

```
[mysqldump]
password=thepass
user=root
```

Restore : 
```
mysql -u root -ptmppassword sugarcrm < /tmp/sugarcrm.sql
```

## Postgres

```bash
$ psql
psql (9.1.18)
Type "help" for help.

postgres=# \du
                              List of roles
  Role name  |                   Attributes                   | Member of 
-------------+------------------------------------------------+-----------
 postgres    | Superuser, Create role, Create DB, Replication | {}

postgres=# \deu+
    List of user mappings
 Server | User name | Options 
--------+-----------+---------
(0 rows)
```
