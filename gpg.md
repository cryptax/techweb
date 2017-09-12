# GPG

## Sign

To sign an email with a given private key:
```bash
$ gpg --clearsign --local-user 0xKeyId doc
```

## Who encrypted a message

```bash
$ gpg --list-only msg.asc
```
