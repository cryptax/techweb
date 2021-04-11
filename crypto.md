# Crypto

## Paddings

### EMSA-PKCS1-v1_5: (signature scheme)

```
	DER encoding of
		DigestInfo ::= SEQUENCE {
			digestAlgorithm AlgorithmIdentifier
			digest OCTET STRING
		}
```
	
`EM=0x00 || 0x01 || 0xff ... 0xff || 0x00 || DER`
	
### RSAES-PKCS1-v1_5: (encryption scheme)

```
k = length of modulus (n)
M: its length must be <= k-11 
EM: length is k.
```

`EM=0x00 || 0x02 || Random bytes ... || 0x00 || M`


### PKCS#7

```
          01 -- if l mod k = k-1
          02 02 -- if l mod k = k-2
                               .
                               .
                               .
          k k ... k k -- if l mod k = 0
```

`l= length input, k= taille du bloc`	


## Certificates

- cer ou .crt: DER Encoded Binary X.509 format or Base 64 Encoded X.509 certificate (DER encoded too I suppose)
- .p7b:	CMS PKCS#7 containing a certificate chain
- .p12 ou .pfx	"Personal Information Exchange" PKCS#12, wrapper of 		DER X.509 certificates.


## RSA

- e*d = 1 mod (p-1)(q-1)
- n = p*q
- e*dq = 1 mod (q-1)
- e*dp = 1 mod (p-1)
- coef = modinv(q) mod p



## Cryptodome

[Cryptodome doc](https://pycryptodome.readthedocs.io)

Import an SSH key:

```python
from Crypto.Util.number import isPrime, GCD, inverse
from Crypto.PublicKey import RSA

k1 = RSA.import_key("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDv9fYADdQjY7ETSi+5ODxXmO2cKJRu4zL7s4yGHLMXVykw3P7PkPOYJ18Q0QZ2mt6hacE1Zw12UmibgjENV4GPR0GR+/N/NZ8t0Vti0hV+Rj3OQij0/W4RM+phTSmnA9Kz4j24ZMNnQAMl7MaOSjHRN+1TE4rETTBMpyKylYu01aGbLbzBBCcW+YeZLhAyYF1FoLyXjSEx6ucDFNE+ud8IrQWts4d50tWFHficRzulfsluo/D1RItasDDx6rtZUSAqWmLWw/XuTmvE4gkU1HsGi9jMnFrAV4sy/s+0jWy+GH/8X7Q1bgfxmX9HfGW3qnO/Kc5eFqX6i9RxnGbC/Yzx alice@work")
```

k1 will have n and e: k1.n, k1.e

To compute GCD: `p = GCD(k1.n, k2.n)`

To divide: `q = k2.n // p`

To test primality: `isPrime(p)`

Modular inverse: `inverse`

To reconstruct a private key: 

```python
p = RSA.construct((k2.n, k2.e, d))
```

