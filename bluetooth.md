# Bluetooth

##

Security modes:

1. No security (security mode 1, level 1)
2. Unauthenticated encryption (security mode 1, level 2)
3. Authenticated encryption (security mode 1, level 3)
4. 


Authorization (to access an attribute):

- No authorization required
- Authorization required


## bluetoothctl

To install bluez-5.5: `sudo apt install libdbus-1-dev libudev-dev libical-dev libreadline-dev`

Power on/off the adapter: `power off`, `power on`

Scanning: `scan on`, `scan off`

```
[!781]$ sudo bluetoothctl
[bluetooth]# scan on
Discovery started
...
```

Connect: `connect xx:xx:xx:xx:xx:xx`

Pair: `[xxxx] # pair  xx:xx:xx:xx:xx:xx`

Agents: see https://www.kynetics.com/docs/2018/pairing_agents_bluez/. `agent NoInputNoOutput`, `agent KeyboardDisplay`

List paired devices: `# paired-devices`

Perform a GATT action: `menu gatt`, then `back` to go back.

Write a characteristic:

```
select-attribute /org/bluez/hci0/dev_xxx/service000c/char0013
write "0xAB 0xCF"
```





## hcitool

In BlueZ 5.50, hcitool no longer exists. Use Bluetoothctl.

```
sudo hcitool lescan
```


## hciconfig

In BlueZ 5.50, hciconfig no longer exists. Use Bluetoothctl.

## hcidump

`sudo apt-get install bluez-hcidump`

```
HCI sniffer - Bluetooth packet analyzer ver 5.37
device: hci0 snap_len: 1500 filter: 0xffffffffffffffff
< HCI Command: Reset (0x03|0x0003) plen 0
> HCI Event: Command Complete (0x0e) plen 4
    Reset (0x03|0x0003) ncmd 1
    status 0x00
< HCI Command: Set Event Filter (0x03|0x0005) plen 1
    type 0 condition 0
    Clear all filters
...
```

## gatttool

In BlueZ 5.50, gatttool no longer exists. Use Bluetoothctl.

- b: BLE mac address
- I: interactive
- t random: random mac address for client

```
sudo gatttool -b xx:xx:xx:xx:xx:xx -I -t random
[xx:xx:xx:xx:xx:xx][LE]> connect
Attempting to connect to xx:xx:xx:xx:xx:xx
Connection successful
[xx:xx:xx:xx:xx:xx][LE]> char-read-hnd 0x0011
Characteristic value/descriptor: 02 12 
```

` sudo gatttool -b xx:xx:xx:xx:xx:xx -I -t random --sec-level=high

Commands:

- `char-read-hnd 0x0011`: read handle 0x11
- `char-write-req 0x0014 ABCD`: write request on 0x14
- `char-read-uid UUID`


## btgatt-client

```
sudo ./btgatt-client --t random -s high -v -d xx:xx:xx:xx:xx:xx
[GATT client]# write-value 0x0014 0xAB 0xCF
...
```

Security level:

```
[GATT client]# get-security
Security level: 1
[GATT client]# set-security 3
Setting security level 3 success
```
Note that despite btgatt-client was claiming security level 3, I had issues where this did not actually correctly set the security level.

## Mirage

- [Repository](https://redmine.laas.fr/projects/mirage)
- [Paper](https://www.sstic.org/media/SSTIC2019/SSTIC-actes/mirage_un_framework_offensif_pour_laudit_du_blueto/SSTIC2019-Slides-mirage_un_framework_offensif_pour_laudit_du_bluetooth_low_energy-alata_auriol_roux_cayre_nicomette.pdf)
- [Doc](http://homepages.laas.fr/rcayre/mirage-documentation/index.html)

### Installation

On Rpi,

```
sudo apt-get install python3-pip
sudo -H pip3 install keyboard psutil pyserial pyusb terminaltables scapy pycryptodomex
```

### Scan

`sudo ~/softs/mirage/mirage_launcher ble_scan` see the device

### Discover

To list services and characteristics:

```
load ble_connect|ble_discover
set ble_connect1.TARGET xx:xx:xx:xx:xx:xx
set ble_connect1.CONNECTION_TYPE  random
set  ble_discover2.GATT_FILE  /tmp/gatt.ini
run
```

**Issue: **security mode is not set.

### Pairing

In `.mirage/mirage.cfg` (on Rpi: /root/.mirage/mirage.cfg)

```
[ble_connect]
TARGET=xx:xx:xx:xx:xx:xx
CONNECTION_TYPE=random

[ble_master]
TARGET=xx:xx:xx:xx:xx:xx
CONNECTION_TYPE=random

[ble_pair]
IRK=112233445566778899aabbccddeeff
BONDING=yes
LTK=112233445566778899aabbccddeeff
CSRK=112233445566778899aabbccddeeff
DISPLAY=yes
KEYBOARD=yes
YESNO=no
SECURE_CONNECTIONS=no
CT2=no
MITM=yes
```

### Ble_master

```
set TARGET xx:xx:xx:xx:xx:xx
set CONNECTION_TYPE random
run
connect
pairing active inputOutput=keyboard
```

or

`pairing active inputOutput=keyboard,display|authentication=bonding,mitm|ltk=112233445566778899aabbccddeeff|rand=1122334455667788|ediv=15555|csrk=112233445566778899aabbccddeeff` or `pairing active inputOutput=keyboard,display|authentication=bonding,mitm,ct2|rand=aedafef17f4a2e5acce6f97b6cd98b4e|ediv=30e5|addr_type=public|addr=aa:bb:cc:dd:ee:ff|ltk=c88d38dbaca0274ca6b84f86939c9c`


## bleah

`sudo python ~/softs/bleah/bin/bleah --enumerate --mac xx:xx:xx:xx:xx:xx`
