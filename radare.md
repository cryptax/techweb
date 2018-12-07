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
- Do not show comments: `e asm.comments=false`
- Go to a given function: `sf sym.xxx`
- Add a function: af ...
- Add a comment: `CC this is my comment @ addr`
- Remove a comment: `CC-`
- Rename a function: `afn new-func-name`
- Rename a local argument: `afvn old-name new-name`
- List entry points: `ie`
- Write to a file: `wtf filename size @ position`
- Shell commands work: `s 0x65; pD 32`


### Print

- Print strings: `ps @ loc`
- Print function: `pdf`

### Search


- Search strings: `iz~STRING`,
- Search in code: `pd @ func~STRING`,
- Search imports: `ii~STRING`,
- Search class names: `ic~STRING`,
- Seach flags (constants, functions, importants): `f~STRING`,
- Search function names: `afl~STRING`

- Save a session: `Ps filename`. By default, sessions are stored in `~/.config/radare2/projects`. To reload a session: `Po filename`


### Visual mode

V then press p to switch between virtual modes

- Enter visual mode: `V`
- Leave visual mode: `q`


# References

- [Reverse Engineering Embedded Software Using Radare2](http://radare.org/get/r2embed-auckland2015.pdf)


