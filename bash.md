# Bash and other Unix tools

## Bash

### Converting

Decimal to hex
```
$ printf "%x" 1234
```

Hex to binary:

- With `xxd -p -r`:
```
$ echo -n "deadbeef" | xxd -p -r | hexdump -C
00000000  de ad be ef                                       |....|
```

- With perl `pack`:
```
$ echo -n "deadbeef" | perl -ne 'print pack "H*", $_' | hexdump -C
00000000  de ad be ef   
```

Note that `hexdump -C` prints exactly as it is in the file, but that hexdump swaps bytes:
```
$ echo -n "deadbeef" | xxd -p -r | hexdump
0000000 adde efbe                              
0000004
```

Instead of `hexdump -C` you can also use `od -t x1`:
```
$ echo -n "deadbeef" | xxd -p -r | od -tx1
0000000 de ad be ef
0000004
```

## Date

Epoch to date: `date -d @1234567890`


## Find

To search for something excluding some paths:

```bash
$ find . -type d -name "blah" ! -path "./softs/*' ! -path "./bin/*"
```

Do not forget the * in the path...


Find files bigger than 10M

```
find . -type f -size +10M
```


## Sed

To remove lines 1-n of a file:
```bash
$ sed '1,nd' file
```




