# Raspberry Pi

## Hardware

Know your version: `cat /proc/cpuinfo`.
Then check [here](https://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/)

Or `cat /proc/device-tree/model`:

```
Raspberry Pi 2 Model B Rev 1.1
```

### Fan

[This explains where to connect the fan](https://castman.fr/wordpress/tag/connecter-le-ventilateur-sur-gpio-raspberry-pi-2-b/). There is nothing more to do: the fan starts when the RPi has booted.


## Installing Raspbian

### Copying the system

- Download Raspbian. For a RPI A+, use the lite edition: `raspbian_lite_latest.zip`
- Unzip it to get, e.g `2018-04-18-raspbian-stretch-lite.img`
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
    ssid="your-ssid"
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

(doesn't exist any longer?)


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


### RAM disk

It is a good idea to have /tmp (and perhaps other directories) as tmpfs.

[Create tmpfs](https://www.hellojona.com/2017/06/create-a-ram-disk-tmpfs-in-raspberry-pi-3/)

## OS

To add a user: `sudo adduser name`.
To add a user to a given group: `sudo adduser login group`

Delete pi user: `sudo deluser -remove-home pi`
Often, this does not work because Pi user is still used to run some process such as lightdm autologin.
The easiest way to get rid of pi user is to run `raspi-config` and in Boot options, select Console mode not GUI (if that is okay), and with no auto login. Then, reboot, and `deluser pi` should work.

### Recalbox

- To install recalbox: `sudo dd if=~/Downloads/recalbox.img of=/dev/sdj bs=32M`
- Recalbox: default root login is `recalboxroot`. This can be secured via the menu and modified to another password.
- Image size: on some TV sets, you may need [overscan](https://github.com/recalbox/recalbox-os/wiki/Overscan-settings-%28FR%29) (**Advanced settings > Overscan : ON**)

#### Installing games

To install games: upload to `/recalbox/share/roms`. You should upload them using the Recalbox Web UI. Go to ROMs and then the correct emulator. Don't forget to click on "restart ES" after you have uploaded (or deleted) games in a given emulator or the action won't be done!

- Sega Mega Drive = Genesis


To install games in the DOS directory, you must follow the instructions in Readme, i.e unzip the files in its own directory named `game.dos` or `game.pc` and inside that, create a file named `dosbox.bat` with the command to launch.

- Stop all emulators: `killall emulationstation`
- High scores for MAME games are located in `/recalbox/share/saves/mame/mame2003/hi`

In MAME, to get more lives: TAB, then DIP Switch.

To play: add credits with **SELECT**

#### Kodi

Kodi exists on Recalbox. It is a *Jarvis* version.

Explains how to install [super repo](https://superrepo.org/get-started/)



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

[How to disable IPv6 on RPi](https://www.leowkahman.com/2016/03/19/disable-ipv6-raspberry-raspbian/)

In /etc/sysctl.conf:  `net.ipv6.conf.all.disable_ipv6 = 1`, then restart `sysctl` with `sudo sysctl -p`

To re-enable, change the setting from 1 to 0, restart sysctl, and put eth0 down and up.

`

### TP-Link USB Wifi Dongle

#### How to install TP-Link Driver - Quick setup

Download the driver (it depends on your kernel):

```
wget http://downloads.fars-robotics.net/wifi-drivers/8822bu-drivers/8822bu-5.4.51-v7l-1333.tar.gz
```

Untar: `tar xvf 8822bu-5.4.51-v7l-1333.tar.gz -C /tmp`

Then:

```
cd /tmp
sudo ./install.sh
sudo reboot
```

#### Understanding how to install (if above does not work)

```
lsusb
Bus 001 Device 004: ID 2357:0115 TP-Link
```


Get the install script:

```
sudo wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi -O /usr/bin/install-wifi
sudo chmod u+x /usr/bin/install-wifi
```

It is a good idea to run the install script to get an idea of which driver you need, but the script is buggy and did not install correctly the driver in my case.

Run the script: `sudo install-wifi`

It says:

```
sudo /usr/bin/install-wifi

 *** Raspberry Pi wifi driver installer by MrEngman.
 *** Performing self-update
 *** Relaunching after update

 *** Raspberry Pi wifi driver installer by MrEngman.

Your current kernel revision = 5.4.51-v7l+
Your current kernel build    = #1333

Checking for a wifi module to determine the driver to install.

Your wifi module is Bus 001 Device 003: ID 2357:0115 TP-Link 

And it uses the 8822bu driver.


Your Pi revision number is c03111
You have a Pi 4 v1.1
Checking for a 8822bu wifi driver module for your current kernel.
There is a driver module available for this kernel revision.
Downloading the 8822bu driver, 8822bu-5.4.51-v7l-1333.tar.gz.
Installing the 8822bu driver.

Installing driver config file 8822bu.conf.
mv 8822bu.conf /etc/modprobe.d/.
Installing driver module 8822bu.ko.
install -p -m 644 8822bu.ko /lib/modules/5.4.51-v7l+/kernel/drivers/net/wireless
Loading and running the 8822bu driver, 8822bu.ko.
```

We are mainly interested in the fact:

1. It detected the USB Wifi Dongle
2. The driver for that dongle is 8822bu.conf
3. The precise package to download is 8822bu-5.4.51-v7l-1333.tar.gz

The install script downloads the package correctly, but then it fails to run it correctly and, in my case,

- `/lib/modules/5.4.51-v7l+/kernel/drivers/net/wireless/8822bu.ko` was empty!
- `/etc/modprobe.d/8822bu.conf` was empty!

Although the files are present in the package...

So, you need to fix that, un-tar the package and copy manually

1. The kernel module
2. The kernel module config file


#### Refs

- Raspbian Forum (people with similar problems, not your exact model): https://www.raspberrypi.org/forums/viewtopic.php?t=57426
- install-wifi script: http://downloads.fars-robotics.net/wifi-drivers/install-wifi



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

### Apache

[Setting up Apache 2 on Raspbian](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)

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

### Minecraft

#### Server 

[How to install](https://raspbian-france.fr/installer-serveur-minecraft-raspberry-pi/). 

- It is indeed very long
- Installed in `/home/axelle/minecraft`

#### Client


[Python in Minecraft](https://raspberry-pi.developpez.com/cours-tutoriels/minecraft/debuter/)

minecraft-pi is a limited version of Minecraft. To play the "real" minecraft, follow [instructions here](https://www.raspberrypi.org/forums/viewtopic.php?t=186547)

At some point you need to download `Minecraft.jar` from a remote server.

```
$ wget --no-check-certificate https://s3.amazonaws.com/Minecraft.Download/launcher/Minecraft.jar
$ java -jar Minecraft.jar
```

In my case, my Java installation was corrupt, and I had to reinstall the JDK 1.8 (`apt-get install --reinstall...`).

As of November 2017, the version of Minecraft is 1.11.2.


