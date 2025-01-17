# Radare2

## Launch commands

- `-w`: open binary in read/write mode
- `-a arm`: specify architecture (`asm.arch`)
- `-b 32`: specify bits (`asm.bits`)
- `-i file`: run script file
- `-m 0x000`: map file at specified address


## Command syntax

- Chain commands: `;` for example `pd 10; px 3`
- Grep: `~`
- Get the first 10 lines of an output: `yourcmd~:0..10`
- Evaluate an expression: `?`. For example, to convert 0x61 to decimal: `? 0x61` will tell you it's 97 and also character `a` etc.
- Here: `$$`
- Relative offsets: `@ $$+x` for example `pd 10 @ $$+4`
- Loop: `@BEGIN!END`: `wox 0x90 @10!20` performs XOR with 0x90 from offset 10 to 20.
- `@@f` iterate over all functions
- Iterations: `@@` for example, write ff at offsets 10, 20, 30 with `wx ff @@10 20 30`



## Configuration properties

- Change architecture: `e asm.arch=arm` or `r2 -a arm...`
- Change bits: `e asm.bits=16`
- Change CPU: `e asm.cpu=cortex`


## Seek

- `s address`
- `s-5`: seek 5 bytes backwards
- `s-`: undo seek
- `afi.`: Go to the beginning of a function (or `sf.`)
- `sf sym.xxx`: Go to function xxx
- `s*`: Show seek history

## Search

- Search strings in the data section: `iz~STRING`,
- Search for a string in disassembly: `pd @ func~STRING`, You can search an entire section that way (but it will be long)
- Search imports: `ii~STRING`,
- Search class names: `ic~STRING`,
- Seach string in flags (constants, functions, importants): `f~STRING`,
- Search name of function: `afl~STRING`

- Search for a string "everywhere": `/ STRING`
- Search for wide-character strings: `/w STRING`
- Search case-insensitive strings: `/i STRING`
- Search for bytes: `/x 04030201` (depending on endianness etc you might need to reverse bytes)
- Search for bytes with some joker (`.`): `/x ab..ef` will skill the 2 middle bytes
- Search for bytes with a pattern: `/x abcdef:ff00ff` does the same as above. The second string is the mask for the pattern.
- Search for instructions: `/ad mov`
- Repeat search: `//`
- Search reference using emulation: `/re`. Ex: search reference using emulation to the current address `/re $$`

Command to run for each hit, to be set with `e cmd.hit`.
For example: `e cmd.hit=px`

## Analyze

- `aa`: Analyze All (all symbolx and entry points), same as running `r2 -A binary`. For a stripped binary, more is usually necessary like `aaa`, `aar`, `aac`...
- `ad`: Analyze data
- `af`: Analyze functions
- `aac`: Find call instructions and assume destination is a function
- `aar`: analyze data references
- `aap`: Search for function preludes

## Functions

- `afl`: List functions. The output is:

1. Address of function
2. The number of basic blocks in the function
3. The size of the function (in bytes)
4. The function's name

*Advanced*: 

- to sort the output and prioritize functions with most references: `afl,xref/sort/dec,1/head/15` (thx to @ApkUnpacker)
- list function tab separated: `afl, :tsv`



- `afn`: Rename function
- `afvn`: Rename local variable
- `afvt`: Change type of local variable
- `axt`: Cross references to
- `axf`: Cross references from
- `afi`: Find the function you are in
- `af` : Define a new function. Go to the beginning of the function, then `af`
- `afx`: See function references


## Strings

- `iz`: strings in the data section
- `izz`: strings in the *whole* binary
- `/az`: search for strings and possibly reconstruct the assembly when they are split

## Sections

- `ie`: List entry point
- `is`: List symbols
- `iS`: List sections
- `ii`: List imports
- `i~strip`: Know if a binary is stripped ("get file info and search for 'strip'")

## Comments

### User comments

- Show all comments: `CC`
- Add a comment: `CC this is my comment @ addr`
- Remove a comment: `CC-`

Comment properties:

- Show opcode description: `e asm.describe=true`
- Do not show comments: `e asm.comments=false`
- Change delimiter: ``e asm.cmt.token=#`

### Automatic instruction comments

Show emulated assembly

- describes CPU opcodes 
- will tell you what value was in this register before and after
- comments on the right of the disassembly
- enable with `e asm.emu = true`
- Read more [Emulating Assembly in Radare2](https://blog.superponible.com/2017/04/15/emulating-assembly-in-radare2/)

Only display useful information concerning the output such as strings the program uses:

- `e emu.str = true` (or 1)

Show [ESIL (Evaluable Strings Intermediate Language)](https://book.rada.re/disassembling/esil.html):
ESIL is Radare2's own intermediate language.

- `e asm.esil = true`

### Defines

- `C- size`: define as code
- `Cd size`: define as data
- `Cs size`: define as string
- `Cf size`: define as struct

## Flags

Flags are labels for offsets: `str` for strings, `sym` for symbols etc.

- `f`: List flags
- `fr`: Rename a flag
- `fs`: Show all flag spaces

Searches are stored in the *search* flag space.
To remove hits: `f- hit*`

## Display

- `ps @ offset`: print string
- `psz @ offset`: print a *zero-terminated* string
- `pdf`: print function
- `px BYTES @ offset`: print x bytes 
- `pxw`: print words
- `pi n @ offset`: print n instructions disassembled
- `pif`: Show only the instructions of a given function (helpful to copy/paste a function)
- `pD n @ offset`: print n bytes disassembled
- Pretty print: `~{}`
- `pcp`: transform the given bytes in a Python array (choose language with `pc?`)
- `p6es text`: base64 encode. `p6ds` to decode
- Show Pico: `?EC yourmessagegoeshere`
- `e scr.pager=more` to get things page by page.

## Zignatures 

Zignatures are recognizable patterns

- Generate zignatures: `zg` (do `aa` before)
- Save zignatures to a file: `zos zigz.z`
- Load zignatures: `zo zigz.z`

## Running ...

- `#!pipe python` to run a Python program with r2
- `? cmd` to evaluate e.g `? 2+3`

## Writing

- Write to a file: `wtf filename size @ position`
- Open a file in write mode: `oo+`
- `wx hex @ offset`: write hex values
- `wa bl 0x20204`: write assembly
- `wox byte`: XOR current block with byte and write it.
- `wox key @ offset length`: XORs length bytes at offset with the key. For the values to be written, you need to enable writing: `e io.cache=true` (or launch `r2` with `-w`)

Advanced:

- `wox 6 @4!10`: XOR from offset 4 to 10 with value 6

## Cryptography

- `poE`/`poD`: encrypt / decrypt with a given algo and key (does not change the binary)
- `/ca algo`: search for magic indicating using of a given algo
- `pFa` (or `pFx`): show decoded ASN.1 / DER certificate

## Session

- Save a session: `Ps filename`. By default, sessions are stored in `~/.config/radare2/projects`. 
- To reload a session: `Po filename`


# Visual mode

V then press p to switch between virtual modes

- Enter visual mode: `V`
- Leave visual mode: `q`


# Radare2 Package Manager: r2pm

- Update: `r2pm update` (or `-U`)
- List all known packages: `r2pm -s`

Install packages:

- Example: `r2pm -i axml2xml`
- Perform a clean install: `r2pm -ci XYZ`

[Ref](https://r2wiki.readthedocs.io/en/latest/tools/r2pm/)

# Rafind

This works on a binary XML (note that `strings --encoding=l` works too):
```
rafind2 -ZS permissions AndroidManifest.xml
```

# Rabin

Show imports:
```
rabin2 -i classes.dex
```

# Rahash

XOR the string with key 0x88

`rahash2 -D xor -S 0x88 -s 'THESTRING' `





# References

- [Reverse Engineering Embedded Software Using Radare2](http://radare.org/get/r2embed-auckland2015.pdf)


