# Samba

- Enumerate shares: `smbclient -L //machine -N
- Enumerate shares with netexec: `netexec smb HOST -u 'username' -p 'password' -d 'domainname' -k --dns-server IPADDR --shares`
- Download all files: `netexec smb HOST -u 'username' -p 'password' -d 'domainname' -k --dns-server IPADDR -M spider_plus -o DOWNLOAD_FLAG=True`

# LDAP

- `ldapsearch -x -H ldap://IPADDR -s base namingContexts`
- `ldapsearch -LLL -x -H ldap://IPADDR -D 'user@blah' -w 'password' -b 'DC=xxx,DC=yyy'`

# Kerberos

- Get TGT: `getTGT.py host/user:'password' -dc-ip IPADDR`
