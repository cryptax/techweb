# Fortigate

## Get system info

```bash
# get system status
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=FD31964)

## Ping

```bash
# execute ping ....
```

## Trace packets

```bash
# diag sniffer packet <interface> <'filter'> <verbose> <count> 
```
(or diagnose)

for example:

```bash
# diag sniffer packet wan1 'tcp port 22' 4 10
# diag sniffer packet dmz none 4 10
# diag sniffer packet internal 'src host 192.168.0.6 and icmp' 4
# diag sniffer packet any 'port 80 or port 8080' 4 0 a
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=11186)



## See IP addresses and MAC addresses

### MAC addresses

`get system arp`

```
Address           Age(min)   Hardware Addr      Interface

192.168.0.4       1          xx:xx:xx:xx:xx:xx root.b
```

https://kb.fortinet.com/kb/viewContent.do?externalId=11717

### Configure IP address

Retrieve URL filters: `show webfilter urlfilter`
Show routing table: `get router info routing-table all`
Show all items: `get`

Configure static route:
```
config route static
edit 1
set gateway ...
set device INTERFACE
```

Configure IP address:

```
config system interface
edit mgmt1
set ip address/x
append allowaccess ssh
...
end
```

### Wifi


Show SSID info: `get wireless-controller vap-status`

```
WLAN: wifi
    name             : wifi
    vdom             : root
    ssid             : fortinet
    downup_oper      : up
    mesh backhaul    : no
    local bridging   : no
    local switching  : yes
    ip               : 192.168.0.xx
    mac              : 00:xxxxxxxxxx
    station info     : 0/0
```

Show interface info:

```
# diagnose wireless-controller wlac -c vap

bssid             ssid                 intf                 wtp-id               vfid:ip-port rId wId
90:6c:ac:xx fortinet             wifi                 FWF61E-WIFI0         ws (0-127.0.0.1:15246) 0 0
```

Show connected clients:

```
diagnose wireless-controller wlac -d sta
```

Disconnect a client: `diagnose wireless-controller wlac kickmac MACADDR`. This does not prevent the client from reconnecting ;)


