# CTF resources


- CyberChef: https://gchq.github.io/CyberChef


## Crypto

- https://blog.cryptohack.org/
- Factorize numbers: http://factordb.com or Unix command `factor`

### AES

```python
from Crypto.Cipher import AES

key = bytes.fromhex('2b7e1...')
iv =    bytes.fromhex('00010203...')
ciphertext = bytes.fromhex('e47bc2d...')

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)
```

### RSA

We have `e*d = 1 mod phi`. This also means there is an int k, such that `e*d = k*phi + 1`.


```python
from Crypto.Util.number import inverse, long_to_bytes, getPrime
from math import gcd

n = int(0x8d926...)
m = b'tototata...'

int_m = bytes_to_long(m)

# d = 1/e mod phi
d_b = inverse(e_b, phi)

# decrypt
plaintext = pow(ciphertext,d_b, n)

p = getPrime(1024)

if gcd(e, phi) == 1:
   print("blah")
   
```

## Communication with a server

```python
from pwn import *

def choice(number):
    p.recvuntil("Choice: ")
    p.sendline(str(number))
```

## Stegano

- Stegsnow: `apt install stegsnow`
- Steghide: steghide.sourceforge.net
- PNG Check and Repair Tool: https://github.com/sherlly/PCRT
- Vigenere Solver: https://www.guballa.de/vigenere-solver


## Write-ups

- https://github.com/sajjadium/ctf-writeups
- https://ret2school.github.io/
- https://github.com/p4-team/ctf

