# Fortigate

## Trace packets

```bash
# diag sniffer packet <interface> <'filter'> <verbose> <count> 
```

for example:

```bash
# diag sniffer packet wan1 'tcp port 22' 4 10
# diag sniffer packet dmz none 4 10
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=11186)
