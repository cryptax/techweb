% Linux 

# Hardware

## Know your hardware

 Before you struggle opening the box or finding the adequate screwdriver, you can try out the following:


List hardware: `lshw` or `inxi -Fxz`
For example:

- Network: `lshw -C network`
- Hard disks: `lshw -C disk`

Product model:
```
$ inxi -M
Machine:   System: xxx product: xxx v: 01
           Mobo: xxx v: x Bios: xx v: xx date: xx/xx/xxxx
```
    or
```
sudo dmidecode -t baseboard | grep -i 'Product'
```


List RAM: `sudo dmidecode -t memory`

List PCI devices: `lspci`.
For example, get the video card:
```
$ lspci -vnn | grep VGA -A 12
```

- list USB devices: lsusb
- list block devices: lsblk
- list SCSI devices (useful for SATA disks): `cat /proc/scsi/scsi` or `lsscsi`

## Get hard disk info

`sudo hdparm -i /dev/sda`

## Monitor luminosity

Get name of device:

```
$ xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1
eDP-1
```

Then set luminosity: `xrandr --output eDP-1 --brightness 0.7`


## Kernel

To list unused kernels:

```
kernelver=$(uname -r | sed -r 's/-[a-z]+//')
dpkg -l linux-{image,headers}-"[0-9]*" | awk '/ii/{print $2}' | grep -ve $kernelver
```

And then, uninstall these images with `sudo apt-get purge linux-image-xxxx`


## Setting keyboard layout

`setxkbmap -layout fr`

## Using accents with a QWERTY layout

Put this in `.profile`: `xmodmap ~/.xmodmaprc` where your `.xmodmaprc` defines your keyboard tricks:

```
! letters

keycode  24 = q Q acircumflex
keycode  25 = w W ecircumflex
keycode  26 = e E eacute
keycode  27 = r R egrave
keycode  30 = u U ucircumflex
keycode  31 = i I icircumflex
keycode  32 = o O ocircumflex

keycode  38 = a A agrave
keycode  40 = d D ediaeresis
keycode  43 = h H ugrave
keycode  44 = j J udiaeresis
keycode  45 = k K idiaeresis
keycode  46 = l L odiaeresis

keycode  52 = z Z adiaeresis
keycode  54 = c C ccedilla


keycode  108 = Mode_switch
```

Alternatively, it is possible to use the "English US International with dead letters" keyboard and then use composition: ` + e gives è. See [here](https://www.ellendhel.net/article.php?ref=2011+09+12-0).

# GRUB

To update the menu image of Grub, edit /etc/default/grub:

```
export GRUB_MENU_PICTURE="/home/xxx.png"
```

Then do `sudo update-grub`

# System

## Services

[Create a service with Systemd](https://doc.ubuntu-fr.org/creer_un_service_avec_systemd)

Example for Junior CTF using CTFd platform:

```
# cat ctfd.service 
[Unit]
Description=Capture The Flag server (CTFd)
After=network-online.target

[Service]
Type=simple
User=root
Group=root
ExecStart=/usr/bin/python /usr/share/CTFd/serve.py &
Restart=on-failure
TimeoutStopSec=300

[Install]
WantedBy=multi-user.target


$ cat ctfd-docker.service 
[Unit]
Description=Docker containers for challenges of Junior CTF
After=ctfd.service

[Service]
Type=oneshot
User=axelle
Group=axelle
RemainAfterExit=yes
ExecStart=/bin/bash /home/axelle/juniorctf/up.sh
ExecStop=/bin/bash /home/axelle/juniorctf/down.sh

[Install]
WantedBy=multi-user.target
```

If you want a service that runs periodically, then use a **timer** (which is a special service) (or use crontab). [This explains how to create a timer](https://www.linuxtricks.fr/wiki/systemd-creer-des-services-timers-unites) (in French).

Basically,

1. Create a service file. The service file dictates the executable to run and in which conditions.
2. Create a timer file (extension .timer) to explain how frequently to run the service.
3. Install the service and timer files to `/lib/systemd/system`
4. Reload: `sudo systemctl daemon-reload`
5. Enable and then activate the timer: `sudo systemctl enable/start xxx.timer`

Example: the service file:

```
[Unit]
Description=Allows kid to log only at certain times of the day
After=graphical.target

[Service]
Type=oneshot
ExecStart=/home/xx/scripts/parentalcontrol.sh

[Install]
WantedBy=multi-user.target
```

The timer file:

```
[Unit]
Description=Allows kid to log only at certain times of the day


[Timer]
OnUnitActiveSec=5min

[Install]
WantedBy=multi-user.target
```

### Commands for Services

- Listing the service config file: `systemctl show SERVICENAME`
- Editing a unit configuration file: `sudo systemctl edit --full SERVICENAME`, then do `sudo systemctl daemon-reload` and finally `sudo systemctl restart SERVICENAME` (see [here](https://www.2daygeek.com/linux-modifying-existing-systemd-unit-file/))
- List failed services: `sudo systemctl list-units --failed`

### Journal for Services

- Dump to a file: `journalctl -x -u service > file`
- Wrap long lines: `journalctl -u service | less` or `journalctl -u service --no-pager`
- After bug `journalctl -xb`


## Network

### Interfaces

```bash 
$ sudo ifconfig <interface> <address> netmask <mask>
```

or with the `ip` syntax use commands such as:

- `ip link set eth0 down`
- `ip address add 192.168.0.77 dev eth0`


### Routes

```bash
ip route show
ip route add 10.20.0.0/24 dev rndis0
ip route add default via 10.20.30.1
```

### Name resolution

In recent Linux Mint / Ubuntu distribution, you no longer directly edit /etc/resolv.conf to specify your name server as the file's header says:

```bash
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
```

Instead, you specify name servers in /etc/resolvconf/resolv.conf.d/base
```bash
$ cat /etc/resolvconf/resolv.conf.d/base
nameserver 4.2.2.2
nameserver 8.8.8.8
nameserver 8.8.4.4
```

If there are some name servers you want to favour, then, you need to put them
in `/etc/resolvconf/resolv.conf.d/head`.

Once this is done, you need to update name resolution with the command `resolvconf -u`.

If you want to add a [DNS server temporarily](https://notes.enovision.net/linux/changing-dns-with-resolve):

1. Add it in `/etc/systemd/resolved.conf`
2. Restart service: `service systemd-resolved restart`
3. Check: `systemd-resolve --status` or `resolvectl`




### Troubleshooting

I had issues with my Ethernet link. In my case, it was solved by commenting out dns=dnsmasq in NetworkManager:

```
[main]
plugins=ifupdown,keyfile,ofono
#dns=dnsmasq

[ifupdown]
managed=false
```

### Wireless

Get your SSID: `iwgetid`

### IPv6

In /etc/sysctl.conf

```
# Disable IPv6
net.ipv6.conf.all.disable_ipv6 = 1
```

### mDNS

*"Avahi is a Linux implementation of Zero Configuration Networking ( Zeroconf ) which implements muticast DNS ( mDNS ) allowing ip address to hostname resolution without the use of standard LAN side DNS services."*

To install it: `sudo apt-get install libnss-mdns`. And ensure that `/etc/nsswitch.conf` has mDNS mentioned:

```
hosts:          files mdns4_minimal [NOTFOUND=return] dns mdns4
```


- avahi requires that port 5353/udp is open.
- To find all IPv4 services on the internal network: ` avahi-browse -at | grep IPv4`
- You can ping `host.local` on the intranet.

### CIFS / AFP

To access a remote Apple Timecapsule:

`sudo mount.cifs //ip/share /mnt/point -o username=theusername,password=thepassword,vers=1.0,sec=ntlm,uid=youruser`

- ip is the IP address of the time capsule
- `share` is the name of the sharepoint on the timecapsule
- `username` and `password` specify the credentials to log on the time capsule
- **do not forget** `vers=1.0` **and** `sec=ntlm`
- uid to specify the Linux user id to give access to

To access a Samba share from a NAS:

`sudo mount -t citfs -o rw,guest,uid=username //ip/share /mnt/point`


### Firewall

`sudo apt install ufw` will install a basic firewall. It won't enable it by default.

- To open port for SSH and HTTPS:

```
ufw allow OpenSSH
ufw allow 'Nginx HTTPS'
```

- To disable a port: `sudo ufw deny 'Nginx HTTP'`
- To list current description: `sudo ufw show added`
- To enable UFW: `sudo ufw enable`
- To list profiles: `sudo ufw app list` (see `/etc/ufw/applications.d`)
- To get the ports of a given profile: `sudo ufw app info PROFILE`



## Locale

```
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
```

`localectl set-locale LANG=en_US.utf8`

## Package management

To re-install a package:

```bash
$ sudo apt-get --reinstall install package
```

### Snap

To restart a service installed via snap:

`sudo snap restart PACKAGE`

## NTP

To list NTP servers I use:

```
$ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*ks3352891.kimsu 138.96.64.10     2 u   99  128  377   37.876   31.229  24.093
...
```

Configure servers to use in `/etc/ntp.conf`

```
# pool: <http://www.pool.ntp.org/join.html>
server ntp.obspm.fr
server ntp.kamino.fr
server ntp2.belbone.be
server 0.fr.pool.ntp.org iburst dynamic
server 1.fr.pool.ntp.org iburst dynamic
server 2.fr.pool.ntp.org iburst dynamic
server 3.fr.pool.ntp.org iburst dynamic
```


To sollicit time: `sudo ntpd -gq`

Or set it manually:

`sudo date -s "3 dec 2017 22:21"`


## SSH

```
ssh-keygen -t rsa -b 4096
ssh-keyscan -H 192.168.0.9 >> known_hosts
```

## SFTP

SFTP comes with SSH! 
I added a `sftp` group, and a `username` user in that group.
Then, in `/etc/ssh/sshd_config`, you need to redirect logins and chroot them to the appropriate dir:

```
Match Group sftp
        ChrootDirectory /var/www/%u
        ForceCommand internal-sftp
```

And strangely, `/var/www/%u` must be owned by *root* not by `biotmeteo`. See [here](https://unix.stackexchange.com/questions/598520/client-loop-send-disconnect-broken-pipe-for-chroot-sftp-user-with-correct-p)

## ZFS

### Install ZFS

On Linux Mint 19:

```bash
sudo apt-get install zfs-dkms zfsutils-linux
```

Then, to import a pool: `zpool import POOLNAME`

## Firewall

```bash
$ iptables -t nat -F ==> flush the NAT table
```

Redirect an IP address to yourself (or another IP address):

```bash
sudo iptables -t nat -A OUTPUT -p all -d SOURCE-IP -j DNAT --to-destination DEST-IP
```

To remove a rule,

1. List rule number: `sudo iptables -t nat -v -L OUTPUT -n --line-number`
2. Remove the given number: `sudo iptables -t nat -D OUTPUT NUM`

Here OUTPUT refers to the part of iptables to work on


```
sudo iptables -t nat -v -L PREROUTING -n --line-number
sudo iptables -t nat --delete PREROUTING 4
```


## LVM

We have:

- physical volumes: e.g. disks or partitions of disks
- volume groups: they have a name and you can add physical volumes to them. e.g you can combine several disks/partitions
- logical volumes:  set its size, its name, where to mount it to and the volume group

Creating a physical volume:

- List the disk you want to use with `lsblk`
- Create a partition (e.g. `fdisk`). Be sure to set partition type `8e` for Linux LVM.
- Create the volume: `pvcreate /dev/sdc1`

Creating the volume group:

- `vgcreate vgelk /dev/sdc1`
- If you want to add future partitions, do `vgextend vgelk /dev/sdc2`. *If the specified PVs have not yet been initialized with pvcreate, vgextend will  initialize  them.*

Creating a logical volume:

- `lvcreate -n var -L 150G vgelk`
- Format the logical volume: `mkfs -t ext4 /dev/vgelk/var`
- Copy the contents of `/var` (or other) to that logical volume:

To shrink a logical volume:

- Do a backup of the volume!
- Unmount it: `sudo umount /your/mountpoint`
- Check filesystem: `sudo e2fsck -fy /dev/mapper/vgpool-docs`
- Resize the filesystem and specify the new size you want it to be (smaller): `sudo resize2fs /dev/mapper/vgpool-docs 15G`
- Resize the logical volume: `sudo lvreduce -L 15G /dev/mapper/vgpool-docs`
- Mount the partition again: `sudo mount /dev/mapper/vgpool-docs /your/mountpoint`

If the idea was to *shrink* a volume to affect the siwe to *another* volume, this works quite easily when both volumes share the same volume group :

1. Extend the logical partition `sudo lvextend -l +100%FREE /dev/mapper/vgpool-video`
2. Run resize to register the new size: `sudo resize2fs /dev/mapper/vgpool-video`

To copy/backup completely a directory (make sure links are ok):
```
mkdir /mnt/var_new
mount /dev/vgelk/var /mnt/var_new
rsync -avHPSAX /var/ /mnt/var_new/
```

- To extend the size of an existing logical volume: `lvextend -L +100G  /dev/mapper/vgpool-xxx`

List:

- Physical volumes: `pvs`
- Volume groups: `vgs`
- Logical volumes: `lvs`

Display info:

- Physical volumes: `pvdisplay`
- Volume groups: `vgdisplay`
- Logical volume: `lvdisplay`


References:

- https://www.computernetworkingnotes.com/rhce-study-guide/learn-how-to-configure-lvm-in-linux-step-by-step.html
- http://www.lerrigatto.com/move-var-to-a-new-partition-with-lvm/

## Consoles

Switch to other consoles with Ctrl-Alt-F1 to F6, and Ctrl-Alt-F7 is graphical.
On a laptop, you often have to add the "Fn" key to get F1 to work, so it would be Ctrl-Alt-Fn-F1.

## User management 

### Adding user to group and take into account immediately

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

## Adding udev rules without rebooting

```bash
sudo udevadm control --reload-rules
sudo service udev restart
sudo udevadm trigger
```

## Cinnamon


- Configure sound levels: `cinnamon-settings sound`
- Lock screen: `cinnamon-screensaver-command --lock`


## Mate

Specify keyboard bindings in `mate-control-center`

## MDM

To have the correct keyboard in MDM, at the end of `/etc/mdm/Init/Default`, insert:

```
/usr/bin/setxkbmap fr
```


# Sound

## Listing devices

```bash
$ sudo aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: PCH [HDA Intel PCH], device 0: ALC269VB Analog [ALC269VB Analog]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
card 1: J20 [Jabra EVOLVE 20], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

or `lspci -v | grep -A7 Audio` or `inxi -A`

```
$ inxi -A
Audio:
  Device-1: Intel 7 Series/C216 Family High Definition Audio driver: snd_hda_intel 
  Device-2: AMD Ellesmere HDMI Audio [Radeon RX 470/480 / 570/580/590] 
  driver: snd_hda_intel 
  Sound Server: ALSA v: k5.4.0-148-generic
```  


## Volume

To set the volume from a terminal: `alsamixer`
To play from the terminal: `paplay file`

## Test

- To test speakers: `speaker-test -Dplug:front -c2`
- Play a test sound: `aplay /usr/share/sounds/alsa/Front_Center.wav`
- See http://mreen.epizy.com/SoundFixTips.html?i=3

# Apps

## Mail

d * removes all email
q

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

## Piwigo

[Piwigo gallery on nginx with debian](https://www.howtoforge.com/install-piwigo-gallery-on-nginx-with-debian-wheezy)

```
create database gallery01; grant all on gallery01.* to 'gallery'@'localhost' identified by 'PASSWORD'; flush privileges; \q;
```

## Yubikey

To use the Yubikey for Linux login: [see YouTube](https://www.youtube.com/watch?v=INi-xKpYjbE)

```
sudo apt update
sudo apt install libpam-u2f
```

Then configure use of the key: `pamu2fcfg > ~/.config/Yubico/yourfile`

For Linux login:, in `/etc/pam.d/lightdm`, insert the line `auth required pam_u2f.so` just after `@include common-auth`:

```
#%PAM-1.0
auth    requisite       pam_nologin.so
auth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin
@include common-auth
auth required pam_u2f.so
-auth    optional        pam_gnome_keyring.so
```

For Linux sudo: do the same in `/etc/pam.d/sudo`:

```
#%PAM-1.0

session    required   pam_env.so readenv=1 user_readenv=0
session    required   pam_env.so readenv=1 envfile=/etc/default/locale user_readenv=0
@include common-auth
auth required pam_u2f.so
```

To use Yubikey for SSH authentication: `sudo apt install libfido2-dev`

Generate a key: `ssh-keygen -t ed25519-sk -C "myyubikey" `

Then copy it to the server: `ssh-copy-id -i ~/.ssh/id_yubikey.pub user@host`

## Certbot

```
sudo apt install snapd
sudo apt install fuse squashfuse
sudo snap install core
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```

- [Renewing](https://tecadmin.net/auto-renew-lets-encrypt-certificates/): `sudo certbot renew --dry-run`  then `sudo certbot renew`. You might need to allow HTTP.

## Owncloud 

Install pre-requisistes:

- `sudo apt-get install apache2 sqlite -y`
- `sudo apt-get install php-mysql php-mbstring php-php-gettext php-intl php-redis php-imagick php-igbinary php-gmp php-curl php-gd php-zip php-imap php-ldap php-bz2 php-phpseclib php-xml`
- `sudo apt install mariadb-server mariadb-client -y`

Prepare:

- In Apache2, serve `/var/www`
- `sudo a2enmod rewrite ` (and restart Apache2)
- Set root password: `sudo mysql_secure_installation`
- Create owncloud user and database:

```
mysql -u root -p
MariaDB [(none)]> create database owncloud;
MariaDB [(none)]> create user owncloud@localhost identified by ‘12345’;
MariaDB [(none)]> grant all privileges on owncloud.* to owncloud@localhost identified by ‘12345’;
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> exit;
```

- Get OwnCloud ZIP: `wget https://download.owncloud.com/server/owncloud-10.11.0.zip`
- `unzip owncloud-10.8.0.zip -d /var/www/`
- `sudo chown www-data:www-data /var/www/owncloud`
- Head to http://your_host/owncloud, and configure
- Enable SSL: `sudo a2ensite default-ssl`

Backup:

- Backup Calendars : `curl -u <username:password> http://<your cloud domain>/remote.php/dav/calendars/<user name>/<calendar name>?export -o calendar.ics` (e.g. `http://127.0.0.1/owncloud/remote.php/dav/calendars/toto/personal?export`)
- Backup Contacts: `curl -u <username:password> http://<host>/owncloud/remote.php/dav/addressbooks/users/<user name>/contacts?export -o contacts`

Config: `/var/www/owncloud/config/config.php`

If you get an untrusted domain warning, in `config.php`, put the correct IP address:

```
'trusted_domains' => 
  array (
    0 => '192.168.0.9',
  ),
```


## Useful packages (at some point...)

- To install glib2:
```
sudo apt-get install libgtk2.0-dev
```


- To install [Java](http://tecadmin.net/install-oracle-java-8-jdk-8-ubuntu-via-ppa/):

`export JAVA_HOME=/usr/lib/jvm/java-8-oracle`
