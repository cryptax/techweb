# Network

## Network Manager

`sudo service network-manager stop`

## ifconfig / ip

Via ifconfig:
```
ifconfig eth0 192.168.2.2 netmask 255.255.255.0 up
route add default gw 192.168.2.1
```

Via ip:
```
ip route show
ip link show wlan1
ip link set br0 address 00:0a:e7:2c:44:2a
sudo ip route del default 
sudo ip route add default via 192.168.0.254 dev eth0
```

## DNS

In `/etc/network/interfaces`, add `dns-nameservers 9.9.9.9 8.8.8.8`.
This is usually now preferred to editing `/etc/resolv.conf` (old method).


## IPv6

In /etc/sysctl.conf:

```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

Reload config with `sysctl -p`

## Wifi

Scan wifi

```
$ sudo iwlist wlan0 scan

 Cell 02 - Address: xxxxx
                    Channel:9
                    Frequency:2.452 GHz (Channel 9)
                    Quality=56/70  Signal level=-54 dBm  
                    Encryption key:off
                    ESSID:"iPhone MyWi"
```


```bash
$ sudo iwconfig wlan0 essid "iPhone MyWi"
$ sudo iwconfig wlan0 ap "02:22:52:26:BC:91"
$ sudo iwconfig wlan0 enc off
$ sudo ifconfig wlan0 up
$ iwconfig wlan1 mode auto
```

via iw:
```
sudo iw dev wlan1 scan
iw dev wlan1 set power_save off
iw dev wlan1 set bitrates 1M
             set frag 2432
	     set rts  2432
	     set distance
sudo iwconfig wlan1 rate 5.5M auto
```


Bridges:

```
sudo brctl addbr br0
sudo brctl addif br0 eth0 wds.wlan1
sudo brctl delbr br0
ifconfig br0 hw ether xx:xx:xx...
```

## DHCP

`sudo dhclient wlan0`


## SNMP

```bash
$ sudo apt-get install snmp
$ snmpbulkwalk -v2c -c public 192.168.0.x
```

## Discovery / scan

```
sudo nmap -sL 192.168.0.0/24
```

## Who listens on this port

Use `ss -tulpn` (better than netstat)

```
sudo ss -tulpn | grep :8000
tcp    LISTEN  0       4096                                             *:8000                                             *:*                                   users:(("docker-proxy",pid=3479,fd=4))              
```


## Which port is used by which process:

`lsof -i -nP`
`iftop -P`

## Test name resolution

`ping -c 1 google.com &> /dev/null && echo success || echo fail`


