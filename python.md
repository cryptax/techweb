# Python

[Key differences between python 2.7 and python 3](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

## Converting...

| From                     |  To                 |  Python 3 |
| ------------------------ | ------------------ | ------------- |
| `h=0x12d687` (hex)      | `1234567` (integer) | `h` (they are the same)|
| `i = 1234567` (integer)   | `'0x12d687'` (string)  | `hex(i)` |
| `i = 1234567` (integer)   | `'12d687'` (string without 0x)  | `'%x' % i` |
| `i=0x1234` (integer) | `b'\x12\x34` (bytes) | `i.to_bytes(2, byteorder='big')` |
| `hexstring='deadbeef'`    | `3735928559` (integer) | `int(hexstring, 16)` |
| `hexstring='deadbeef'`    | `b'\xde\xad\xbe\xef'` (bytes) | `bytes.fromhex(hexstring)` |
| `hexstring='de ad be ef'` | `b'\xde\xad\xbe\xef'` | `bytes.fromhex(hexstring)` |
| `hexstring='deadbeef'`    | `bytearray(b'\xde\xad\xbe\xef')` (bytearray) | `bytearray.fromhex(hexstring)` |
| `b=b'\xde\xad\xbe\xef'` (bytes) |  `'deadbeef'` (string) | `b.hex()` |
| `b=bytearray(b'\xde\xad\xbe\xef')` (bytearray) |  `'deadbeef'` (string) | `b.hex()` |
| `b=bytearray(b'\xde\xad\xbe\xef')` (bytearray)  | `[222, 173, 190, 239]` (list) | `list(b)` |
| `l=[222, 173, 190, 239]` (list) | `b'\xde\xad\xbe\xef'` (bytes) | `bytes(l)` |
| `n=97` (ascii value) | `'a'` (character) | `chr(n)` |
| `c='a'` (character) |  `97` (ascii value) | `ord(c)` |
| `s='cryptax'` (string) |  `b'cryptax'` (bytes) | `bytes(s, 'utf-8')` |
| `b=b'cryptax'` (bytes) | `'cryptax'` (string) | `b.decode('utf-8')` |


### Time

```python
import time
time.gmtime(123456)
```

From epoch to localtime:

`time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1428316200))`

From local time to epoch:

`print time.mktime(time.strptime("10.08.2015 00:00:00", "%d.%m.%Y %H:%M:%S"))`

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

## Virtual env

https://www.pythoncentral.io/how-to-install-virtualenv-python/

Installing virtualenv:

1. `easy_install pip`
2. `pip install virtualenv`

Creating a virtual env: `virtualenv name`. By default, uses `--no-site-packages` options (otherwise: `--use-site-packages`). To specify a particular Python interpreter, use option `-p /usr/bin/pythonX`.

Activate: `source bin/activate`
Deactivate: `deactivate`

To use ipython of the virtual env: `alias ipy="python -c 'import IPython; IPython.terminal.ipapp.launch_new_instance()'"`

With python3, `python3 -m venv`

# Setup.py

Sample setup.py:

```python
#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'droidlysis',
    description='Short description'
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='your name',
    author_email='your email',
    url='a URL',
    license='MIT',
    keywords="android malware reverse",
    python_requires='>=3.0.*',
    version = '3.0.13',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Operating System :: Unix",
    ],
    install_requires=[ 'configparser', 'python-magic', 'SQLAlchemy', 'rarfile' ],
    scripts = [ 'yourpythonscripts.py' ]
)
```

To add data files, add `include_package_data=True` and a `MANIFEST.in` file:

```
include conf/*.conf
```




- Create source package: `python3 setup.py sdist`
- Upload package to test pypi: `twine upload --repository-url https://test.pypi.org/legacy/ dist/package-x.y.z.tar.gz`
- Test install using test pypi: `pip3 install --no-cache-dir --extra-index-url https://test.pypi.org/simple/ package`

