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


## Gogs

- To use SSH, make sure git account has a `/home/git` home dir + SSH server allows use of `authorized_keys`.
- See https://discuss.gogs.io/t/how-to-config-ssh-settings/34
