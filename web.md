# Web

## curl

- Set headers with **-H**: `curl -H "Host: blah" website`
- Do not verify certificate: **-k**
- Post data: `-d "param=1&arg=2"`

## dig

- Get only MX records: `dig mx website`
- Get DNS config using a given DNS: `dig @ns-provider.net www.example.com`

## nmap

- Get list of available ciphers: `nmap --script ssl-cert,ssl-enum-ciphers -p 443 website`

```
nmap --script ssl-cert,ssl-enum-ciphers -p 443 www.example.com

Starting Nmap 7.01 ( https://nmap.org ) at 2019-04-05 14:04 CEST
...
PORT    STATE SERVICE
443/tcp open  https
...
| ssl-enum-ciphers: 
|   TLSv1.2: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
|     compressors: 
|       NULL
|     cipher preference: server
|_  least strength: A

Nmap done: 1 IP address (1 host up) scanned in 1.33 seconds
```

## Hosting a Web site with Flask

- Install Flask: `pip3 install flask`
- Create the Flask application:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
...
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context='adhoc', threaded=True, debug=True)
```

- Install Gunicorn: `pip3 install gunicorn`
- Test it works with `gunicorn`: `gunicorn --access-logfile - --workers 2 --bind 0.0.0.0 'app:create_app()'`
- Create a system service:

```
[Unit]
Description=gunicorn daemon for Picoweb
After=network.target

[Service]
User=axelle
Group=axelle
WorkingDirectory=/home/axelle/picoweb
ExecStart=/home/axelle/.local/bin/gunicorn --access-logfile - --workers 2 --bind 0.0.0.0 'app:create_app()'

[Install]
WantedBy=multi-user.target
```
- Copy the file to `/etc/systemd/system/`
- Enable the service: `sudo systemctl enable picoweb.service`
- Start the service: `sudo systemctl start picoweb.service`
- Check you can access the service locally 
- Install nginx: `sudo apt install nginx`
- Configure your site in nginx for HTTP: in `/etc/nginx/conf.d` (e.g `picoweb.conf`):

```
server {
       server_name	YOUR_DOMAIN;

       location / {
       		proxy_pass http://127.0.0.1:8000;
	}
```
- Restart nginx: `sudo systemctl reload nginx`, `sudo systemctl restart nginx`
- Make sure your domain redirects to your host IP address port 80
- Check you can access the web site via http://YOUR_DOMAIN

## Get a certificate with Let's Encrypt

- Get a certificate with Let's Encrypt. Install [Certbot](https://certbot.eff.org). Make sure there are no OS `certbot` packages, if so, uninstall them `sudo apt-get remove certbot` as we are installing Cerbot via SNAP.

```
sudo apt install snapd
sudo apt install fuse squashfuse
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```

To renew a certificate:

```
sudo certbot renew --dry-run
sudo certbot renew
```

- You should now be able to access https://YOUR_DOMAIN

## Hugo

```
hugo new site mysite
cd mysite/themes
```
