# GDB

```
gdb ./programtodebug
```

## Display, investigation

List source code:

- If debugging symbols are present, you can use `layout src`.
- Otherwise, `layout asm`
- List from line x to y: `l x,y`

Address spaces

- Mapped address spaces: `info proc map`
- List functions and their address: `info functions`
- Info on registers: `info r`

Show values:

- `p xxx`. For example `p $edi`.
- Specify `/x` for hex value, `/t` for binary, `/d` for unsigned int: `print /x value`
- Display memory: `x/60x addr` where 60 is the length you want to display and `x` is the format (hex)

Show the stack:

- `bt`
- `p $sp`

Disassemble:

- `disassemble funcname`

Searching:

- `searchmem hex start end`

```
gdb-peda$ searchmem 0x4141 0x406000 0x427000 
Searching for '0x4141' in range: 0x406000 - 0x427000
Not found
```

## Running, breaks etc

- `run $(perl -e 'print "A"x80)`


- Breakpoint. `b line`
- To set a variable: `set var=value`
- Get the type of a variable: `whatis var`

```
(gdb) whatis f
type = struct fp *
```

- Step through an instruction: `si`
- `next`


## Little Endianness

- Say you write "\x55\x55\x51\xa9" to 0x5555555592f0. Then you get:

```
0x5555555592f0:	0xa9515555
```

## Core dump

To enable: `uclimit -c unlimited`

- Load it: `./gdb prog core`
- Dump memory: `objdump -s core`
