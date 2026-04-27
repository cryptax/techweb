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

To write hex in a binary at a given position:

```
echo "00000088: 0000 4000" | xxd -r - modified.elf
```

To read it back: `xxd -s 0x88 -l modified.elf`


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

- Epoch to date: `date -d @1234567890`
- Get epoch: `date "+%s"`
- Given date to epoch: `date -d '2024-03-03T06:00' +%s`


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

## Awk

Swapping 2 columns in a file:

```
 awk -F, '{print $2,$1}' OFS=, file
```


## Convert

Creating an image with text "Blah"

```
convert -background white -fill dodgerblue  -font "FreeMono" -strokewidth 2  -stroke blue   -undercolor lightblue -size 165x70 -gravity center label:Blah image.png
```

## Cut

Get given characters: `cut -c15-22`

## Renaming files


Renaming `.txt` extension files to `.text`:

```
for f in *.txt; do 
    mv -- "$f" "${f%.txt}.text"
done
```
## Tar

Untar selectively:

```
tar -xzf lotsofdata.tar.gz --wildcards --no-anchored '*contract*'
```

## Auto-completion in Bash

https://github.com/akinomyoga/ble.sh

```
# Quick INSTALL to BASHRC (If this doesn't work, please follow Sec 1.3)

curl -L https://github.com/akinomyoga/ble.sh/releases/download/nightly/ble-nightly.tar.xz | tar xJf -
bash ble-nightly/ble.sh --install ~/.local/share
echo 'source -- ~/.local/share/blesh/ble.sh' >> ~/.bashrc

```

## Oh my Posh

- https://ohmyposh.dev/
- install meslo nerd font: `oh-my-posh font install meslo`
- Update fonts: `fc-cache -fv`
- Configure the font in Terminator
- In .bashrc, setup my theme:

```bash
# oh my posh
eval "$(oh-my-posh init bash --config ~/.config/oh-my-posh/croctheme.omp.json)"
```


This is a modification of gruvbox theme:

```json
{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "blocks": [
    {
      "alignment": "left",
	"segments": [
	    {
		"background": "#2f7e10",
		"foreground": "#ffffff",
		"style": "powerline",
		"template": "{{ .UserName }}@{{ .HostName }}",
		"type": "session"
	    },
            {
		"background": "#2f7e10",
		"foreground": "#ffffff",
		"powerline_symbol": "\ue0b0",
		"options": {
		    "style": "full"
		},
		"style": "powerline",
		"template": " {{ .Path }} ",
		"type": "path"
            },
            {
		"background": "#f4cfa0",
		"background_templates": [
		    "{{ if or (.Working.Changed) (.Staging.Changed) }}#f4cfa0{{ end }}",
		    "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#ff4500{{ end }}",
		    "{{ if gt .Ahead 0 }}#B388FF{{ end }}",
		    "{{ if gt .Behind 0 }}#B388FF{{ end }}"
		],
		"foreground": "#282828",
		"leading_diamond": "\ue0b6",
		"powerline_symbol": "\ue0b0",
		"options": {
		    "branch_template": "{{ trunc 25 .Branch }}",
		    "fetch_status": true,
		    "branch_icon": "\uE0A0 ",
		    "branch_identical_icon": "\u25CF"
		},
		"style": "powerline",
		"template": " {{ .HEAD }}{{if .BranchStatus }} {{ .BranchStatus }}{{ end }}{{ if .Working.Changed }} \uf044 {{ .Working.String }}{{ end }}{{ if and (.Working.Changed) (.Staging.Changed) }} |{{ end }}{{ if .Staging.Changed }} \uf046 {{ .Staging.String }}{{ end }}{{ if gt .StashCount 0 }} \ueb4b {{ .StashCount }}{{ end }} ",
		"trailing_diamond": "\ue0b4",
		"type": "git"
            },
            {
		"background": "#FFDE57",
		"foreground": "#111111",
		"powerline_symbol": "\ue0b0",
		"options": {
		    "display_mode": "files",
		    "fetch_virtual_env": false
		},
		"style": "powerline",
		"template": " \ue235 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
		"type": "python"
            },
            {
		"background": "#ffff66",
		"foreground": "#111111",
		"powerline_symbol": "\ue0b0",
		"style": "powerline",
		"template": " \uf0ad ",
		"type": "root"
            }
	],
	"type": "prompt"
    }
  ],
    "console_title_template": "{{ .Folder }}",
    "final_space": true,
    "version": 4
}
```
