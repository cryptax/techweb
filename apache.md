# Apache

## Differences between 2.2 and 2.4

[Differences between Apache 2.2 and 2.4](https://wiki.apache.org/httpd/ClientDeniedByServerConfiguration)

2.2:

```xml
<Directory /var/www/example.com>
  Order allow,deny
  Allow from all
</Directory>
```

2.4:

```xml
<Directory /var/www/example.com>
  Require all granted
</Directory>
```



## Set up HTTPS

```
a2enmod ssl
a2ensite default-ssl
sudo make-ssl-cert generate-default-snakeoil --force-overwrite
a2dissite 000-default
```

In /etc/apache2/ports.conf

```xml
#NameVirtualHost *:443
#Listen 80

<IfModule mod_ssl.c>
    # If you add NameVirtualHost *:443 here, you will also have to change
    # the VirtualHost statement in /etc/apache2/sites-available/default-ssl
    # to <VirtualHost *:443>
    # Server Name Indication for SSL named virtual hosts is currently not
    # supported by MSIE on Windows XP.
    NameVirtualHost 192.168.0.10:443
    Listen 443
</IfModule>

<IfModule mod_gnutls.c>
    Listen 443
</IfModule>
```

## Solve "Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName"

/etc/hosts:

```
127.0.0.1       localhost.localdomain localhost legumic
192.168.0.9     legumic
```
