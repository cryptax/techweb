# Fortigate

## Console access

`screen /dev/ttyUSB0 9600`

## CLI help

- show
- show full: to get all values including the current default ones
- tree

## Get system info

```bash
# get system status
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=FD31964)

Get info on hardware:

```
# config global
# diag hardware test info
```

Get info on TPM:

```
config global
diagnose hardware deviceinfo tpm
diag tpm get-property 0 
```

Get info on Bluetooth

```
config global
diag bluetooth status
```

Get IPv6 sessions: `diag sys session6 list`

## Ping

```bash
# execute ping ....
```

(or `exec ping`)

Ping fortiguard servers: 

```
execute ping service.fortiguard.net
execute ping update.fortiguard.net
execute ping guard.fortinet.net
```

## Setting Transparent mode

```
config system settings
    set opmode transparent
    set inspection-mode flow
    set manageip 192.168.0.99/255.255.255.0
    set gui-ips enable
    set gui-endpoint-control disable
    set gui-dnsfilter disable
end
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
# diagnose sniffer packet any ' host 255.255.255.255 and udp and port 67 or port 68' 4 0 a
```

[KB Fortinet](http://kb.fortinet.com/kb/viewContent.do?externalId=11186)

## DNS

`show system dns`, or to edit: `config system dns`

```
# show system dns
config system dns
    set primary 96.45.45.45
    set secondary 96.45.46.46
    set protocol dot
    set server-hostname "globalsdns.fortinet.net"
end

```

## Debug

```
diagnose debug application update -1
diagnose debug enable
diagnose debug disable
```

## Update

`execute update-now`

To debug an issue with update:

```
diagnose debug application update -1
diagnose debug enable
execute update-now
```

wait for the update to happen, check logs, and then `diagnose debug disable`

## Regenerate local certificates

1. Backup configuration
2. In the configuration file, look for the section `config certificate local`
3. Erase completely the section.
4. Restore the config. The fortigate will re-generate all missing certificates.


## List files on the filesystem

```
# fnsysctl ls -l /etc/cert/factory
-rw-r--r--    1 0        0       Thu Sep 19 11:47:49 2024             5174 root_Fortinet_Factory.cer
-rw-r--r--    1 0        0       Sat Feb  8 12:05:04 2025             1854 KEY-FILE
-rw-r--r--    1 0        0       Thu Sep 19 11:47:49 2024             4285 root_Fortinet_Factory_Backup.cer
-rw-r--r--    1 0        0       Sat Feb  8 12:05:04 2025             1854 root_Fortinet_Factory_Backup.key

```

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

The different bandwidths etc: [here in French](https://siam.lyon.archi.fr/index.php/informatique/materiels/431-wifi-normes)

[FortiAP and wifi configuration guide](https://docs.fortinet.com/document/fortiap/7.0.0/fortiwifi-and-fortiap-configuration-guide/307228/defining-a-wireless-network-interface-ssid)

Get Wifi country:

```
FWF-Home-Ax # config wireless-controller setting

FWF-Home-Ax (setting) # show
config wireless-controller setting
    set country FR
    set darrp-optimize-schedules "default-darrp-optimize"
end
```


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

```bash
# diagnose wireless-controller wlac -c vap

bssid             ssid                 intf                 wtp-id               vfid:ip-port rId wId
90:6c:ac:xx fortinet             wifi                 FWF61E-WIFI0         ws (0-127.0.0.1:15246) 0 0
```

Show connected clients:

```
diagnose wireless-controller wlac -d sta
```

Disconnect a client: `diagnose wireless-controller wlac kickmac MACADDR`. This does not prevent the client from reconnecting ;)


# FortiAP with Fortigate in Transparent mode

Connect directly to the FortiAP using a switch (or a cross cable):

- Set your host's IP address for example to 192.168.1.3
- Connect to the FortiAP on `http://192.168.1.2`. This is its default factory address
- Modify the AC_IPADDR (fortigate), the gateway (e.g. box, router...) and default IP address. Apply.
- Verify the modifications have been performed.

Then, un-wire the FortiAP and connect it to the FortiGate.

- Check the FortiAP will connect on the Network interface "internal" hardware switch. Check this interface has CAPWAP support.
- Go to Wifi, Managed FortiAPs, you should see it appear after a while (needs to boot). Authorize it.
- Set the SSID etc.

To [set the country](https://kb.fortinet.com/kb/viewContent.do?externalId=FD35116)

```
config wireless-controller setting
set country GB
```


