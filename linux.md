% Linux 

# System

## Network

### Interfaces

```bash 
$ sudo ifconfig <interface> <address> netmask <mask>
```

### Routes

```bash
ip route show
ip route add 10.20.0.0/24 dev rndis0
ip route add default via 10.20.30.1
```

## Package management

To re-install a package:
```bash
$ sudo apt-get --reinstall install package
```

## Firewall

```bash
$ iptables -t nat -F ==> flush the NAT table
```

## Adding user to group and take into account immediately

1. Add user to new group B.
2. Get the current group of the user:
```bash
$ id -g
```
Let's call that group A.
3. Change group to B:
```bash
$ newgrp B
```
4. Reset back to original group:
```bash
$ newgrp A
```



# Apps

## Recording desktop

```
$ gtk-recordmydesktop
```

To stop: Ctrl-Mod-s

## Bluez

```bash 
$ wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.20.tar.xz
$ tar -xvf bluez-5.20.tar.xz
$ cd bluez-5.20/
$ sudo apt-get install libudev-dev libical-dev libreadline-dev
$ ./configure –enable-library –disable-systemd
$ make
$ make check
$ sudo make install
$ sudo cp attrib/gatttool /usr/bin/
$sudo cp tools/btmgmt /usr/bin/
```
