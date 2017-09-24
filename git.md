# Git

## Import a directory

```bash
cd existing_folder
git init
git remote add origin https://blah.git
git add .
git commit
git push -u origin master
```

## Configuration

```
git config pack.windowMemory 10m
git config pack.packSizeLimit 20m
git config pack.threads 1
```
