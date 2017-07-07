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
