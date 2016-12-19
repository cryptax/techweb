# Bash and other Unix tools

## Find

To search for something excluding some paths:

```bash
$ find . -type d -name "blah" ! -path "./softs/*' ! -path "./bin/*"
```

Do not forget the * in the path...

## Sed

To remove lines 1-n of a file:
```bash
$ sed '1,nd' file
```
