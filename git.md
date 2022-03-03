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

- Get a particular commit for a file: `git checkout xxxx file`. This is just to *test* a given commit.
- To revert the last commit: `git revert xxxxx`. See [here](https://code.likeagirl.io/how-to-undo-the-last-commit-393e7db2840b)
- Return from a detached HEAD state: `git checkout master` or `git checkout -`

## Branches

Create the new branch:

```
git checkout master
git branch new-branch
git checkout new-branch
```

Then code, and commit on the new branch.

Finally, when you need to merge:

```
git checkout master
git merge new-branch
```

This merges everything locally. Solve merge conflicts.
Finally:

```
git push origin master
```

To remove a remote branch: `git push -d origin BRANCHNAME`

To list remote branches:

```
git fetch
git branch -a
```

To switch to a branch: `git checkout branchname`


## Gogs

- To use SSH, make sure git account has a `/home/git` home dir + SSH server allows use of `authorized_keys`.
- See https://discuss.gogs.io/t/how-to-config-ssh-settings/34

Example of SSH config file `~/.ssh/config`:

```
Host github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa_xxxx
```    
