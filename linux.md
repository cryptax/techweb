# Linux notes

## Hardware

### Know your hardware

 Before you struggle opening the box or finding the adequate screwdriver, you can try out the following:

1. **lshw**

- Network: `lshw -C network`
- Hard disks: `lshw -C disk`

2. **inxi**

- List all: `inxi -Fxz`
- Product model: `inxi -M`
- Graphic card: `inxi -G`
- Audio: `inxi -A`

3. **dmidecode**

- Product: `sudo dmidecode -t baseboard | grep -i 'Product'`
- List RAM: `sudo dmidecode -t memory`

4. **lspci**

- Video card: `lspci -vnn | grep VGA -A 12`
- Audio: `lspci -v | grep -A7 Audio`

5. `lsusb`, list block devices: `lsblk`, list SCSI devices (e.g SATA disks): `cat /proc/scsi/scsi` or `lsscsi`

6. Hard disk info: `sudo hdparm -i /dev/sda`

7. Audio: `sudo aplay -l`


### Control monitor 

Get name of device:

```
$ xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1
eDP-1
```

- Set the resolution: `xrandr --output DP-3-1 --mode 2560x1440`
- Set luminosity: `xrandr --output eDP-1 --brightness 0.7`

### Keyboard layout CLI

`setxkbmap -layout fr`

To have the correct keyboard in **MDM**, at the end of `/etc/mdm/Init/Default`, insert:

```
/usr/bin/setxkbmap fr
```

- Specify keyboard bindings in `mate-control-center`

Using accents with a QWERTY layout:

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

## Sound 

- To set the volume from a terminal: `alsamixer`
- To play from the terminal: `paplay file`

- To test speakers: `speaker-test -Dplug:front -c2`
- Play a test sound: `aplay /usr/share/sounds/alsa/Front_Center.wav`
- See http://mreen.epizy.com/SoundFixTips.html?i=3



## Kernel

To list unused kernels:

```
kernelver=$(uname -r | sed -r 's/-[a-z]+//')
dpkg -l linux-{image,headers}-"[0-9]*" | awk '/ii/{print $2}' | grep -ve $kernelver
```

And then, uninstall these images with `sudo apt-get purge linux-image-xxxx`

To solve [this error](https://forums.debian.net/viewtopic.php?t=152806), add to `/etc/modprob.d/blacklist.conf`, and then 
`update-initramfs -u`

```
blacklist btrfs
blacklist mdraid
blacklist raid6_pq
```


## GRUB

**NB.** All edits to `/etc/default/grub` must be "committed" afterwards with `sudo update-grub` to take them in account.

- Update the menu image of Grub, `export GRUB_MENU_PICTURE="/home/xxx.png`
- See boot logs: remove `quiet splash` from `GRUB_CMDLINE_LINUX_DEFAULT`
- Fix ACPI boot error "ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.GP17.VGA.LCD._BCM.AFN7], AE_NOT_FOUND=": add `acpi_backlight=vendor` to `GRUB_CMDLINE_LINUX_DEFAULT`

## Boot

- See boot logs: `dmesg -T` or `/var/log/boot.log`, or `journalctl -b`
- Investigate slow boot:

```
systemd-analyze blame
systemd-analyze critical-chain
```

## Systemd / systemctl

### Create a service

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

- Listing the service config file: `systemctl show SERVICENAME` ou `systemctl cat SERVICENAME`
- Editing a unit configuration file: `sudo systemctl edit --full SERVICENAME`, then do `sudo systemctl daemon-reload` and finally `sudo systemctl restart SERVICENAME` (see [here](https://www.2daygeek.com/linux-modifying-existing-systemd-unit-file/))
- List failed services: `sudo systemctl list-units --failed`

On peut également créer des services "utilisateurs" qui sont stockés dans `~/.config/systemd/user`. Ensuite, on peut utiliser les commandes `systemctl` et `journalctl` avec l'option `--user`, et sans sudo.

Exemple: `systemctl --user status mega-cmd-server`

### Journal for Services

- Dump to a file: `journalctl -x -u service > file`
- Wrap long lines: `journalctl -u service | less` or `journalctl -u service --no-pager`
- After bug `journalctl -xb`
- List boot logs: `journalctl -b`


## Autofs

To automatically mount a filesystem, use autofs.
For example, here I am automatically mounting in `/mnt/ticot`:

`/etc/auto.master`:

```
/mnt /etc/auto.ticot --timeout=120
```

`/etc/auto.ticot`:

```
ticot -fstype=cifs,rw,guest, ://IP ADDRESS/Data
```


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

#### List DNS servers

With Linux Mint, to view current DNS server: `nmcli dev show | grep DNS`

#### Test name resolution

To test name resolution, we can use `dig` or `resolvectl`:

```
dig linux.org @8.8.8.8
resolvectl query linux.org
```

For a compact result for resolution, query A records with `dig`:

```
$ dig +nocmd google.com a +noall +answer @8.8.8.8
google.com.		300	IN	A	142.250.179.110
```

#### Edit DNS servers

In recent Linux Mint / Ubuntu distribution, you no longer directly edit `/etc/resolv.conf` to specify your name server as the file's header says:

```bash
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
# 127.0.0.53 is the systemd-resolved stub resolver.
# run "systemd-resolve --status" to see details about the actual nameservers.
```

Rather, you configure DNS servers for  your link.
Note that `systemd-resolve` has been renamed to `resolvectl` in systemd 239.

There are DNS servers for:

- Global: those are default DNS servers to use when the current interface hasn't been configured with any DNS server. The DNS servers for this link are configured via `/etc/systemd/resolved.conf`. If you want to enforce those DNS servers to be used for all network interfaces (old and new ones), [follow this guideline](https://andrea.corbellini.name/2020/04/28/ubuntu-global-dns/)
- Each network interface. The DNS servers for each link are configured either by a GUI, or by its CLI `nmcli`

#### Editing DNS servers via nmcli (for each interface)

To edit DNS servers: `nmcli connection modidy <Connnection name> ipv4.dns "ip1 ip2 ..."`. 

- IP addresses should be separated by a space
- This replaces all DNS servers with those specified. If you want to *add* a DNS server use `+ipv4.dns`
- The connection name is the value of `GENERAL.CONNECTION`.

```
GENERAL.CONNECTION:                     Wired connection 1
```


You need to reactivate the connection for the changes to take effect:

```
$ nmcli con down "Wired connection 1"
Connection 'Wired connection 1' successfully deactivated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/7)

$ nmcli con up "Wired connection 1"
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/8)
```

[Nmcli commands details](https://access.redhat.com/documentation/fr-fr/red_hat_enterprise_linux/7/html/networking_guide/sec-using_the_networkmanager_command_line_tool_nmcli)

#### Editing the global DNS servers

1. Edit `/etc/systemd/resolved.conf`
2. Restart service: `sudo systemctl restart systemd-resolved`
3. Check: `resolvectl`



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

### NFS v4

Mount it:

`sudo mount -t nfs4 IPADDR:PATH MNTPOINT`

In `/etc/fstab`:

-  `IPADDR:PATH DIRWHERETOMOUNT nfs rw,vers=4,soft,intr 0 0`



To list possible export points:

- `showmount -e IPADDR`




### Firewall

#### ufw

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


#### iptables

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

#### Reverse SSH, RDP, xxx

If a firewall on your network blocks ports you need or multiplexes an IP address, you might want to use **reverse** x/y. Such services are offered by some hosts like [serveo](https://serveo.net).

- On the server: `ssh -R myalias:22:localhost:22 serveo.net`. Change myalias with something you want.
- On another host, access the SSH server with `ssh -J serveo.net user@myalias`. Note that `-J` means "Connect to the target host by first making a ssh connection to the jump host described by the destination and then establishing a TCP forwarding to the ultimate destination from there."




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

## Adding udev rules without rebooting

```bash
sudo udevadm control --reload-rules
sudo service udev restart
sudo udevadm trigger
```

To disable card readers for example, add `/etc/udev/rules.d/99-disable-card-readers.rules`. Precisely, this adds the tag `UDISKS_IGNORE` to the readers.

```
SUBSYSTEM=="block",ENV{ID_MODEL}=="CF_Card_CF", ENV{UDISKS_IGNORE}="1"
SUBSYSTEM=="block",ENV{ID_MODEL}=="MS_Card_MS", ENV{UDISKS_IGNORE}="1"
SUBSYSTEM=="block",ENV{ID_MODEL}=="SM_XD_Card_SM", ENV{UDISKS_IGNORE}="1"
SUBSYSTEM=="block",ENV{ID_MODEL}=="SD_Card_MMC_SD", ENV{UDISKS_IGNORE}="1"
```

Use `sudo udevadm info -n /dev/sdf` to find the `ID_MODEL` of the devices to disable. Then, they can still be mounted with `mount /dev/sdX ...`. Note that ID_MODEL cannot be used with a rule < 50.

- `udevadm info -e` to see all devices and all environment variables


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

- To remove a repository: `add-apt-repository --remove <repository_name>`

### Snap

To restart a service installed via snap:

`sudo snap restart PACKAGE`

## Consoles

Switch to other consoles with Ctrl-Alt-F1 to F6, and Ctrl-Alt-F7 is graphical.
On a laptop, you often have to add the "Fn" key to get F1 to work, so it would be Ctrl-Alt-Fn-F1.

## User management 

Adding user to group and take into account immediately

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


## Window Manager

- To stop: `sudo init 3` (alternative: `sudo killall /usr/bin/X`)
- To resume: `sudo init 5`


**Cinnamon**


- Configure sound levels: `cinnamon-settings sound`
- Lock screen: `cinnamon-screensaver-command --lock`
- To set the login window: `sudo lightdm-settings `


## Apps

- [PasswordSafe](https://sourceforge.net/projects/passwordsafe/)

If no bluetooth on the motherboard: `sudo apt-get remove --auto-remove pulseaudio-module-bluetooth`

### Emacs

```
sudo apt install elpa-imenu-list
M-x package-refresh-contents followed by M-x package-install RET elpy RET.
sudo apt install elpa-py-autopep8
```

### Mail

d * removes all email
q

### NTP

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


To manually synchronize with time of a different server:

```
sudo timedatectl set-ntp false
sudo ntpdate servername
```

To use NTP again and for sync:

```
sudo timedatectl set-ntp true,
sudo systemctl restart systemd-timesyncd,
sudo timedatectl timesync-status
```




### Oathtool

`gpg --quiet --decrypt your.secret.totp.asc | oathtool --base32 --totp -`


## Recording desktop

```
$ gtk-recordmydesktop
```

To stop: Ctrl-Mod-s



### SSH

```
ssh-keygen -t rsa -b 4096
ssh-keyscan -H 192.168.0.9 >> known_hosts
```

### SFTP

SFTP comes with SSH! 
I added a `sftp` group, and a `username` user in that group.
Then, in `/etc/ssh/sshd_config`, you need to redirect logins and chroot them to the appropriate dir:

```
Match Group sftp
        ChrootDirectory /var/www/%u
        ForceCommand internal-sftp
```

And strangely, `/var/www/%u` must be owned by *root* not by `biotmeteo`. See [here](https://unix.stackexchange.com/questions/598520/client-loop-send-disconnect-broken-pipe-for-chroot-sftp-user-with-correct-p)


### Piwigo

[Piwigo gallery on nginx with debian](https://www.howtoforge.com/install-piwigo-gallery-on-nginx-with-debian-wheezy)

```
create database gallery01; grant all on gallery01.* to 'gallery'@'localhost' identified by 'PASSWORD'; flush privileges; \q;
```

### Yubikey

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

### Certbot

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

### Owncloud 

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

### Nut

[Nut](https://networkupstools.org) controls UPS devices and hosts which depend on the UPS device for its power.

You need [different components whether your host is *physically* attached to the UPS, or if it just needs the UPS for its power](https://networkupstools.org/docs/user-manual.chunked/Configuration_notes.html#UPS_shutdown). 

Therefore, we are going to install *NUT* `sudo apt install nut` on several hosts: those attached to a UPS, and those which needs the power of the UPS, and sometimes both. This is configured by the *NUT mode*:

- standalone is used for a host which is attached to a UPS + needs it for its power.
- netmonitor is used for a host which just needs the UPS for its power.


#### Hardware

Plug the UPS device on USB. It should be immediately visible to `dmesg` and `lsusb`.

```
$ lsusb | grep UPS
Bus 001 Device 005: ID 0463:ffff MGE UPS Systems UPS
```

#### Configuration

| Service | Binary  | Configuration file | Comments |
| ------- | ------- | ------------------ | -------- |
| nut-server |      | /etc/nut/nut.conf | |
|         | `upsdrvctl` | `/etc/nut/ups.conf` | UPS driver |
|         | `upsd` | `/etc/nut/upsd.conf` | UPS information server |
| nut-monitor | `upsmon` | `/etc/nut/upsmon.conf` | UPS monitoring |


- **NUT mode** is specified in `/etc/nut/nut.conf`. Use the `standalone` mode for the host onto which the UPS is physically attached (and `netmonitor` for one which just needs power from the UPS). As the documentation says "this implies to start the 3 NUT layers (driver, upsd and upsmon) and the matching configuration files.

```
MODE=standalone
```


- **Driver**. The driver is started/stopped by `upsdrvctl`

```
$ sudo upsdrvctl start
Network UPS Tools - UPS driver controller 2.7.4
Network UPS Tools - Generic HID driver 0.41 (2.7.4)
USB communication driver 0.33
Using subdriver: MGE HID 1.39
```

Driver is configured in `/etc/nut/ups.conf`, add the **driver** to your UPS. One section per UPS.  For example:

```
[myups]
 	driver = mydriver
	port = /dev/ttyS1
	cable = 1234
	desc = "Something descriptive"
```  

- **Udev**. In `/etc/udev/rules.d/90-ups.rules`, adjust *idVendor* and *idProduct* depending on what `lsusb` reports for the UPS device. Then restart udev: `sudo service udev restart`

```
ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="0463", ATTR{idProduct}=="ffff", MODE="0660", GROUP="nut"
```

- **UPS information server**. The server is responsible for serving the data from the drivers to the clients.  It is started by the service `nut-server` and concerns binary `upsd`.

UPS server configuration is in `/etc/nut/upsd.conf`. The most basic configuration consists in adding the IP address and port: `LISTEN 127.0.0.1 3493`. Access configuration is in `/etc/nut/upsd.users`, create accounts for the UPS server:


```
[username]
password = "PASSWORD"
actions = SET
actions = FSD
instcmds = ALL
upsmon master
```

- **UPS monitoring configuration**. It is controlled by the `nut-monitor` service and concerns `upsmon` binary. In `/etc/nut/upsmon.conf`. In particular, when the UPS reaches a Low Battery event, the primary `upsmon` (ie. the one on the host attached to the UPS) sets a FSD (= Forced ShutDown) flag to tell all slave systems that it will soon power down the load. [The full cycle is detailed here](https://networkupstools.org/docs/user-manual.chunked/Configuration_notes.html#UPS_shutdown).

```
POWERDOWNFLAG /etc/killpower
MONITOR eaton@localhost 1 <username> <password> <master|slave>
MINSUPPLIES 1
SHUTDOWNCMD "/sbin/shutdown -h +0"
```

Note that it is normal to get an "Login on UPS [myups] failed - got [ERR ACCESS-DENIED]" for nut-monitor on the host which has the nut server (can't both listen and connect).

To log UPS events, add this to `upsmon.conf`

```
NOTIFYFLAG ONLINE	SYSLOG+WALL
NOTIFYFLAG ONBATT	SYSLOG+WALL
NOTIFYFLAG LOWBATT	SYSLOG+WALL
NOTIFYFLAG FSD	SYSLOG+WALL
NOTIFYFLAG COMMOK	SYSLOG+WALL
NOTIFYFLAG COMMBAD	SYSLOG+WALL
NOTIFYFLAG SHUTDOWN	SYSLOG+WALL
NOTIFYFLAG REPLBATT	SYSLOG+WALL
NOTIFYFLAG NOCOMM	SYSLOG+WALL
```

The logs go in `/var/log/daemon.log`. For example:

```
$ sudo tail -n 1000 /var/log/daemon.log | grep -iE "ups|nut"
Feb  8 11:40:49 vegan upsmon[31836]: UPS eaton@localhost on battery
Feb  8 11:42:19 vegan upsmon[31836]: UPS eaton@localhost on line power
Feb  8 11:44:33 vegan upsd[16403]: User legumic@192.168.0.9 logged into UPS [Eaton]
Feb  8 12:14:59 vegan upsd[16403]: User legumic@192.168.0.9 logged into UPS [Eaton]
```


#### Starting NUT

```
$ sudo systemctl restart nut-server 
```

Or simply to reload configuration file: `sudo upsd -c reload`





#### Commands

A few administration tools are supplied:

- **upsc**: lightweight UPS client.
- **upscmd**: UPS administration program for *instant commands*
- **upsrw**: UPS variable administration tool

Examples: 

- To list UPS units configured on the system: `upsc -L`
- To list configuration of the UPS unit: `upsc <MYUPS>`, or `upsrw <MYUPS>`
- To list clients connected to a UPS unit: `upsc -c <MYUPS>`
- To list instant commands supported on a UPS: `upscmd -l <MYUPS>`
- To check a given instant command: `upsc <MYUPS> ups.beeper.status`. 
- Get the status of a given UPS: 

```
upsc eaton ups.status
OL
```

Status meaning:

- OL: online
- LB: low battery

Note that if the UPS server is remote, <MYUPS> should be in format `myups@host`

- Check when there has been power cuts etc: `grep -i ups /var/log/daemon.log` (on each system)

Troubleshooting or testing:

- Test shutdown sequence *without shutting down*: `sudo upsdrvctl -t shutdown`

#### UPS references

- https://gist.github.com/dieechtenilente/b8823ce10479d63b6ecab1ef2c7ebc8f
- https://srackham.wordpress.com/2013/02/27/configuring-nut-for-the-eaton-3s-ups-on-ubuntu-linux/
- https://www.ipfire.org/docs/addons/nut/detailed
- [Disable UPS beeps under Linux](https://linux-tips.com/t/disabling-ups-beep-under-linux/592)
- [Status values](https://www.ullright.org/ullWiki/show/ubuntu-nut-ups-with-eaton-3s)


### Useful packages (at some point...)

- To install glib2:
```
sudo apt-get install libgtk2.0-dev
```


- To install [Java](http://tecadmin.net/install-oracle-java-8-jdk-8-ubuntu-via-ppa/):

`export JAVA_HOME=/usr/lib/jvm/java-8-oracle`
