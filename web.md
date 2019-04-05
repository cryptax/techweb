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

