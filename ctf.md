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

## Write-ups

- https://github.com/sajjadium/ctf-writeups
- https://ret2school.github.io/
- https://github.com/p4-team/ctf

