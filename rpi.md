# Raspberry Pi

## Firmware

Update firmware:

```
rpi-firmware update
```

## Bluetooth

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
[bluetooth]# pair aa:aa:aa...
bluetooth]# connect aa:aa:aa...
Attempting to connect aa:aa:aa...
[CHG] Device aa:aa:aa... Connected: yes
Connection successful
```

## OS

Delete pi user: `sudo deluser -remove-home pi`

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

