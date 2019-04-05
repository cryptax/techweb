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

## Reverting

- Get a particular commit for a file: `git checkout xxxx file`
- Return from a detached HEAD state: `git checkout master` or `git checkout -`
