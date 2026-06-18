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

## Pcap

- Output as JSON
- Process pcap with `dpkt` in Python.

```python
import dpkt
with open("capture.pcap", "rb") as file:
    pcap = dpkt.pcap.Reader(file)
```	


## Stegano

- Stegsnow: `apt install stegsnow`
- Steghide: steghide.sourceforge.net
- PNG Check and Repair Tool: https://github.com/sherlly/PCRT
- Vigenere Solver: https://www.guballa.de/vigenere-solver
- Drawing with Python: PIL, Image and ImageDraw

## Pwn

### x86

- RAX: return value of a function
- RDI, RSI, RDX, RCD: arguments of a function
- RSP: stack pointer - where to write on the stack
- RBP: base pointer. Points to the "base" of the stack.
- RIP: instruction pointer. Points to the next instruction. When a RET is executed, it pops the address from the stack in RIP.

When you call a new function:

1. Push the return address on the stack
2. Jump to function entry

```
--------------
Return address
Top of new stack <--- RSP
--------------
```

The beginning of the new function usually does:

- save old base pointer
- set new base pointer
- allocate local variables

```
--------------
Return address
Save base pointer <--- RBP
Local 1          <---- RSP
--------------
```

When you return, 

- free local variables
- restore previous base pointer
- pop saved return address in RIP

```
High addr
| Saved ret addr | 
|----------------|
| Saved RBP      | 
|----------------|
| Local buffers  |
Low addr
```

Stack alignment:

- 16 bytes on x86-64
- 4 bytes on x86-32


### Gef

- Gef: https://github.com/hugsy/gef
- `checksec`: show protections of the binary
- `pattern create 50`: generate a 50-byte pattern. Then `pattern search $rsp`
- `info functions [keyword]`: list functions (matching the keyword)
- `info variables`: list variables
- `disassemble func`
- `x/s addr`: examine string at this address
- `x/20i $rip`: disassemble 20 instructions at RIP
- `run < filename` or `run $(pattern create 200)`

### Pwntools

- https://github.com/Gallopsled/pwntools
- p64(0x401146): write the correct byte string (for little endian). For big endian, use p64((0x401146, endian='big')
- pwntools with gdb: https://halb.it/posts/pwntools-gdb/

## OSINT tools

- [dumpor.io](https://dumpor.io/) which provides a general overview of several social media accounts for a given login.
- [Gmail OSINT tool](https://gmail-osint.activetk.jp/) 


## Web challenges

- Get a cookie file with `-c`. It's a plaintext cookie. To re-use it later, use `-b`:

```
curl -i -c /tmp/cte33216-auth.txt \
  -d 'username=test317619&email=test317619@x.test&password=test123' \
  -X POST \
  http://URL
```

- Enumerating directories of a website: **gobuster**. Download a list, [example](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt)

```
gobuster dir \
  -u URL 
  -w /tmp/directory-list-2.3-medium.txt \
  -c 'session=YOURCOOKIE' \
  -b 404 \ # hide responses with 404
  -t 30 # 30 threads
```

- Test typical Jinja injections like `{{7*7}}`. `--data-urlencode with encode special characters. `-sS` is for silent mode.

```
curl -sS -b /tmp/cte33216-auth.txt \
  --data-urlencode 'username={{7*7}}' \
  -X POST \
  http://URL
```

- *Abuse* Python globals and imports: example: `self.__init__.__globals__.__builtins__.__import__('os').popen('id').read()`

- Making the server think you're local:

```
curl -s \
  -H "X-Forwarded-For: 127.0.0.1" \
  -H "X-Real-IP: 127.0.0.1" \
  -H "X-Forwarded-Host: localhost" \
  -H "CF-Connecting-IP: 127.0.0.1" \
  -b /tmp/vip_cookies.txt \
  http://URL
```

**JWT** (JSON Web Token) consists in `header.payload.signature`. For example,

- Header: `{ "alg": "HS256", "typ" : "JWT" }`
- Payload: `{ "username" : "me", "is_admin" : "true"} `
- Signature: `Base64( HMAC-SHA256(secret, HEADER.PAYLOAD) )`. Uses a JWT **secret**.

In Python, use `import jwt`, then:

```python
token = jwt.encode( { "username" : "me", "is_admin" : "true"}, SECRET, algorithm="HS256")
return jsonify(token=token)

...

try:
   payload = jwt.decode( request.cookies.get("token") or request.headers["Authorization"].removeprefix("Bearer "), SECRET, algorithms=["HS256"})
except (jew.InvalidTokenError, KeyError):
   ...
```




## Write-ups

- https://github.com/sajjadium/ctf-writeups
- https://ret2school.github.io/
- https://github.com/p4-team/ctf

