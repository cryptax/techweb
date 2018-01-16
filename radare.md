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


- Go to a given function: `sf sym.xxx`
- Add a comment: `CC this is my comment @ addr`
- Remove a comment: `CC-`
- Rename a function: `afn new-func-name`
- List entry points: `ie`
- Search strings: `iz~STRING`, search in code: `pd @ func~STRING`, search imports: `ii~STRING`, search class names: `ic~STRING`, flags (constants, functions, importants): `f~STRING`, search function names: `afl~STRING`
- Save a session: `Ps filename`. By default, sessions are stored in `~/.config/radare2/projects`. To reload a session: `Po filename`

Visual mode:

- Enter visual mode: `V`
- Leave visual mode: `q`

