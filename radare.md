# Radare2

## Plugins

```
r2pm init
r2pm -i axml2xml
```

## Rafind

This works on a binary XML (note that `strings --encoding=l` works too):
```
rafind2 -ZS permissions AndroidManifest.xml
```

## Rabin

Show imports:
```
rabin2 -i classes.dex
```

## r2

- Change architecture: `e asm.arch=arm` or `r2 -a arm...`
- Change bits: `e asm.bits=16`
- Change CPU: `e asm.cpu=cortex`
- Use *emulated assembly* `e asm.emu=true` then `aae` [see here](https://blog.superponible.com/2017/04/15/emulating-assembly-in-radare2/)
- Do not show comments: `e asm.comments=false`
- Go to a given function: `sf sym.xxx`
- Add a function: af ...
- Add a comment: `CC this is my comment @ addr`
- Find the function you are in: `afi`
- Remove a comment: `CC-`
- Rename a function: `afn new-func-name`
- Rename a local argument: `afvn old-name new-name`
- Define a function: go to the function beginning then `af`
- Go to the beginning of a function: s `afi.` or `sf.`
- List entry points: `ie`
- Write to a file: `wtf filename size @ position`
- Shell commands work: `s 0x65; pD 32`
- Cross references: `axf` or `axt`. Function references: `afx`
- Load predefined binary structure: `r2 -nn file`
- Open a file in write mode: `oo+`
- Save a session: `Ps filename`. By default, sessions are stored in `~/.config/radare2/projects`. To reload a session: `Po filename`

### Print

- Print strings: `ps @ loc`
- Print function: `pdf`
- Print hexa: `px NUM @ loc` to display NUM bytes

### Search


- Search strings: `iz~STRING`,
- Search in code: `pd @ func~STRING`, You can search an entire section that way (but it will be long)
- Search imports: `ii~STRING`,
- Search class names: `ic~STRING`,
- Seach flags (constants, functions, importants): `f~STRING`,
- Search function names: `afl~STRING`
- Search for bytes: `/x 04030201` (depending on endianness etc you might need to reverse bytes)

### XOR

Do it from Radare2 entirely. Beware, this *modifies* the executable:

```
e io.cache=true
wox 0x88 @ str.mystring // 88 = 0x88 is the key
px 20 @ str.mystring
```

The other solution is to use `rahash2`

`rahash2 -D xor -S 0x88 -s 'THESTRING' `

### Visual mode

V then press p to switch between virtual modes

- Enter visual mode: `V`
- Leave visual mode: `q`


# References

- [Reverse Engineering Embedded Software Using Radare2](http://radare.org/get/r2embed-auckland2015.pdf)


