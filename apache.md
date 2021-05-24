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

- Enable SSL Apache module: `a2enmod ssl`

AFAIK, your `/etc/apache2/ports.conf` should like this:

```xml
Listen 80

<IfModule ssl_module>
	Listen 443
</IfModule>

<IfModule mod_gnutls.c>
	Listen 443
</IfModule>
```

- Create certificate. If you need a self signed certificate, you can use openssl: `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt`, or you can use the Debian wrapper tool `sudo make-ssl-cert generate-default-snakeoil --force-overwrite`

- Enable the website: `a2ensite THESITE` (e.g default-ssl). You need to reload or restart Apache2 afterwards.
- To disable: `a2dissite THESITE`

## Solve "Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName"

/etc/hosts:

```
127.0.0.1       localhost.localdomain localhost legumic
192.168.0.9     legumic
```
