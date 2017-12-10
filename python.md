# Python

## Converting...

| Type    | Example |
| ------- | ------- |
| Integer | `i = 1231232131` |
| Hexadecimal | 0x64 |
| Hex string | '49631c83' |
| String  | 'cryptax' |
| Character | 'c' = '\x63' |
| Byte    | 0x0b |
| Byte string | '\x0b' |
| Byte array | `[0xde, 0xad, 0xbe, 0xef]` |

- Get **ASCII** value of a character: `ord('\x0b') = 0x0b = 11`
- Get character


### int to hex string

Just use print conversion: 

```python
i = 1231232131
"%x" % i
```

### hexstring to int value e.g "3012" -> 0x3012 = 12306

Use `int` and specify base:

```python
hexs = '3012'
i = int(hexs, 16)
```

### string or byte string to byte array (and reciprocally)

Using `map(ord, ...)`: 

- `map(ord, 'cryptax')` is `[99, 114, 121, 112, 116, 97, 120]`
- `map(ord, '\xde\xad\xbe\xef')` is `[222, 173, 190, 239]`

`list(bytearray(...))` gives the same result.

Reciprocally, use `map(chr, ...)` and `join` to get rid of the array:


`''.join(map(chr,[0xde, 0xad, 0xbe, 0xef]))` is '\xde\xad\xbe\xef'
or
`''.join([chr(x) for x in [0xde, 0xad, 0xbe, 0xef]])`

### Hex string to byte array

`fromhex` accepts a hex string, with spaces or not:

- `list(bytearray.fromhex("deadbeef"))` is `[222, 173, 190, 239]`
- same for `list(bytearray.fromhex("de ad be ef"))`

Reciprocally,

- `''.join(map(chr,[0xde, 0xad, 0xbe, 0xef])).encode('hex')` is `deadbeef`

### Time

```python
import time
time.gmtime(123456)
```

From epoch to localtime:

`time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1428316200))`

From local time to epoch:

`print time.mktime(time.strptime("10.08.2015 00:00:00", "%d.%m.%Y %H:%M:%S"))`



### String to hex string with no spaces (and reciprocally)

- `'cryptax'.encode('hex')` is `'63727970746178'`
- `'\xde\xad\xbe\xef'.encode('hex')` is `deadbeef`


Reciprocally: `hexstring.decode('hex')`


## XOR

```python
from itertools import izip, cycle
import string

def xor(message, key):
   return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(message, cycle(key)))

key = 'THEKEY'
xor(buffer, key)
```

## Base64

To do base64 with a different alphabet:

```python
import string
crypt_alphabet="./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
std_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
s = s.translate(string.maketrans(crypt_alphabet, std_alphabet)
base64.b64decode(new_s)
```

## Interactive shell

`ipython`: `%page l`

## Filter

```python
l = d.get_strings()
filter(lambda x:'http' in x, l)
```

## Markdown

This is an easy way to convert markdown syntax to HTML using Python:

```
sudo pip install markdown
python -m markdown blah.md > blah.html
```

## Add system logs

```python
syslog.syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_USER)
syslog.syslog(syslog.LOG_WARNING, "keyboard interrupt")
```
