# Network

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
```

## SNMP

```bash
$ sudo apt-get install snmp
$ snmpbulkwalk -v2c -c public 192.168.0.x
```

## Discovery / scan

```
sudo nmap -sL 192.168.0.0/24
```
