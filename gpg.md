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

## For who the message is encrypted

`gpg --list-packets file`


## Signing keys

Sign a key: `gpg --sign-key`

Remove the signature of key: 

```
gpg --edit-key user-id
> minimize

```
