# Fortigate

## Get system info

```bash
# get system status
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=FD31964)

## Trace packets

```bash
# diag sniffer packet <interface> <'filter'> <verbose> <count> 
```

for example:

```bash
# diag sniffer packet wan1 'tcp port 22' 4 10
# diag sniffer packet dmz none 4 10
# diag sniffer packet internal 'src host 192.168.0.6 and icmp' 4
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=11186)

## See IP addresses and MAC addresses

`get sys arp`


```
# get sys arp

Address           Age(min)   Hardware Addr      Interface

192.168.0.4       1          xx:xx:xx:xx:xx:xx root.b
```
