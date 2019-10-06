# Raspberry Pi

## Installing Raspbian

### Copying the system

- Download Raspbian. For a RPI A+, use the lite edition: `raspbian_lite_latest.zip`
- Unzip it to get `2018-04-18-raspbian-stretch-lite.img`
- Insert a SD card, and run `lsblk` to spot where it is located
- Copy raspbian on the SD card: `sudo dd bs=4M if=2018-04-18-raspbian-stretch-lite.img of=/dev/sdX conv=fsync` where sdX is for example `sdj` (but not `sdj1`)

With a lite Raspbian, the operation might take a few minutes.

Note [it is possible to combine the Unzip and the copy](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md) with `unzip -p` and a pipe.

### Customizing the image (eg headless systems)

Once the image  has been copied on the SD card, We need to reload the partition table for the SD card: `sudo partprobe /dev/sdX`. Then you will notice two partitions on the SD card:

```
$ sudo fdisk /dev/sdj

Command (m for help): p

...
   Device Boot      Start         End      Blocks   Id  System
/dev/sdj1            8192       96453       44131    c  W95 FAT32 (LBA)
/dev/sdj2           98304     3637247     1769472   83  Linux

```

Mount the 1st partition: `sudo mount /dev/sdj1 /mnt/usbstick/`. This corresponds to the `/boot` partition.


To **enable SSH** at startup: `sudo touch /mnt/usbstick/ssh`

To **configure Wifi**, create a file `/mnt/usbstack/wpa_supplicant.conf`. At startup, this file will be copied in the correct directory automatically.

```

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=fr

network={
    ssid=your-ssid
    psk="your key use wpa_passphrase"
    key_mgmt=WPA-PSK
}
```

See [Headless setup](https://raspberrypi.stackexchange.com/questions/10251/prepare-sd-card-for-wifi-on-headless-pi)



## Firmware

Update firmware:

```
rpi-firmware update
```

## Multiboot

NOOBS supports multi boot. Partitions typcally have the following layout.

Partitions:

| Partition | Description |
| ----------| ----------- |
| /dev/mmcblk0p1 | NOOBS boot partition - that's where the Pi boots |
| /dev/mmcblk0p2 | Extended partition |
| /dev/mmcblk0p5 | NOOBS settings |
| /dev/mmcblk0p6 | Boot partition of OS1 |
| /dev/mmcblk0p7 | OS1 |
| /dev/mmcblk0p8 | Boot partition of OS2 |
| /dev/mmcblk0p9 | Recalbox |

In `/dev/mmcblk0p5`, 

```
$ cat noobs.conf 
[General]
default_partition_to_boot=8
display_mode=0
keyboard_layout=fr
language=us
```

To reboot to OS1:

```
echo 6 > /sys/module/bcm2709/parameters/reboot_part
```

To reboot to OS2:

```
echo 8 > /sys/module/bcm2709/parameters/reboot_part
```

Or to reboot to NOOBS:

```
echo 0 > /sys/module/bcm2709/parameters/reboot_part
```

See [here](https://github.com/recalbox/recalbox-os/wiki/Setup-a-dual-boot-raspbian-recalboxOS-(EN)) to setup multi boot.
Note this is not possible yet with Recalbox 6.0


## OS

To add a user: `sudo adduser name`.
To add a user to a given group: `sudo adduser login group`
Delete pi user: `sudo deluser -remove-home pi`

### Recalbox

To install recalbox: `sudo dd if=~/Downloads/recalbox.img of=/dev/sdj bs=32M`

Recalbox: default root login is `recalboxroot`. This can be secured via the menu and modified to another password.

To install games in the DOS directory, you must follow the instructions in Readme, i.e unzip the files in its own directory named `game.dos` or `game.pc` and inside that, create a file named `dosbox.bat` with the command to launch.



## Network 

### Setting a static IP address

In `/etc/network/interfaces`

```

auto lo

iface lo inet loopback
iface eth0 inet static
      address x.y.z.w
      netmask 255.255.255.0
      gateway 192.168.0.254
      dns-nameservers	8.8.8.8	4.2.2.1
```

Then, make sure to disable DHCP:

```
apt-get remove dhcpd
update-rc.d dhcpd disable

```

### Disabling ipv6

[How to disable IPv6 on RPi3](https://no-sheds.blogspot.fr/2017/05/disabling-ipv6-on-raspberry-pi.html)

/etc/modprobe.d/ipv6.conf:

```
alias net-pf-10 off
alias ipv6 off
options ipv6 disable_ipv6=1
blacklist ipv6
```

In `/boot/cmdline.txt`:


```
ipv6.disable=1 dwc_otg.lpm_enable=0 ...
```

### Bluetooth

#### Scan for bluetooth devices

```bash
$ bluetoothctl
[NEW] Controller xx:
[NEW] Device yy:yy
bluetooth]# power on
Changing power on succeeded
[bluetooth]# agent on
Agent registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# help
bluetooth]# scan on
Discovery started
[CHG] Controller zz:zz:zz... Discovering: yes
```

#### Pair a controller

```
[bluetooth]# pair aa:aa:aa...
```

To pair with an 8bitdo controller, press its right button (bottom)

#### Connect to a device

```
[bluetooth]# connect aa:aa:aa...
Attempting to connect aa:aa:aa...
[CHG] Device aa:aa:aa... Connected: yes
Connection successful
```

#### Other commands

info


## Apps

### Kodi

[Install Kodi](http://kodi.wiki/view/HOW-TO:Install_Kodi_on_Raspberry_Pi#Raspbian)

```
sudo apt-get update
sudo apt-get install kodi
```

### VLC

```
sudo apt-get install vlc
```

### OwnCloud

[Install OwnCloud 8](http://www.framboise314.fr/installer-owncloud-8-sur-un-raspberry-pi-2/)


### Arduino

Add user to dialout group

### PiVPN

[PiVPN](http://www.pivpn.io/): the install is straight forward but a bit long (even on Rpi3).
Then, do not forget to open port UDP 1194 on the firewall and box.

To create a profile, use the `pivpn --add` command.
To list current connections, `pivpn -c`.
To list existing profiles, `pivpn -l`.

Then, on the client, it's very simple:

- Linux: `openvpn -c xxx.ovpn`
- Android: install OpenVPN app, and import .ovpn profile



