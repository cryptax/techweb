% Android

# Shell commands

```bash
adb shell am start -a android.intent.action.DIAL -d "tel:*%2306%23"
adb emu sms send 1234 hello from here
adb shell dumpsys iphonesubinfo 
adb shell dumpsys cpuinfo
```

get the Android ID:
```bash
adb shell settings get secure android_id
```


# Android SDK

```bash
$ android list sdk --extended -a
```

# Reverse tethering

[Reverse tethering](http://forum.xda-developers.com/showthread.php?t=2287494)

# Install a CA certificate

```bash
openssl genrsa -out .http-mitm-proxy/keys/ca.private.key 2048
openssl rsa -in .http-mitm-proxy/keys/ca.private.key -pubout > .http-mitm-proxy/keys/ca.public.key
openssl req -x509 -new -nodes -key .http-mitm-proxy/keys/ca.private.key -days 1024 -out .http-mitm-proxy/certs/ca.pem -subj "/C=US/CN=Blah"
```

Then, [follow this link](http://wiki.cacert.org/FAQ/ImportRootCert#Android_Phones_.26_Tablets):

```bash
openssl x509 -inform PEM -subject_hash_old -in root.crt | head -1
openssl x509 -inform PEM -text -in root.crt -out /dev/null >> 5ed36f99.0
mount -o remount,rw /system
cp /sdcard/5ed36f99.0 /system/etc/security/cacerts/
cd /system/etc/security/cacerts/
chmod 644 5ed36f99.0
reboot
```

# Motorola Moto E 4G specifics

Concerns a Motorola Moto E 4G (LTE) 2nd generation XT1524.

- Recovery partition: 	TWRP
- System 	CyanogenMod 13

## Unlocking the bootloader

Get adb and fastboot if you don't have them yet.

```bash
sudo apt-get install android-tools-fastboot
```

On the phone,:

-  go to Settings Dev Settings, And Select Allow OEM Unlock
-  go to developer options allow USB debugging

On the computer, make sure adb access works: add the device to /etc/udev/rules.d/99-adb.rules (use lsusb to know how):

```
SUBSYSTEM=="usb", ATTR{idVendor}=="22b8", OWNER="axelle", GROUP="plugdev", MODE="666"
```

Restart udev:

```bash
$ udevadm control --reload-rules
$ udevadm trigger
```

Then,

-  Make sure the device has full battery (or at least 70% is recommended)
-  Shutdown the device, disconnect USB cable if any
-  Connect USB cable
-  Put your device in fastboot mode (power off, then press the power and volume down buttons simultaneously). Normally it will boot in a special mode and say it is connected.

From computer, get unlock code:

```bash
$ fastboot oem get_unlock_data
...
(bootloader) xxxxxxxxxx#xxxxxxxxxxxxxxxx
(bootloader) xxxxxxxxxxxxxxxxxxxxx#xxxx
(bootloader) xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
(bootloader) xxxx#xxxxxx00000000000000000
(bootloader) 0000000
OKAY [  0.236s]
finished. total time: 0.236s
````

- Remain in fastboot mode
- Go to [motorola site](https://motorola-global-portal.custhelp.com/app/standalone/bootloader/unlock-your-device-a), and request unlock key . For that, you'll need to copy/paste the unlock data.
 -  For the Motorola Moto E phone I got this unlock code (sent by email afterwards):

```
Unlock Code: xxxxxxxxxxxxx
```

- Send the unlock code from PC to smartphone:

```bash
$ fastboot oem unlock xxxxxxxxxxxxxx
...
(bootloader) Unlock code = xxxxxxxxxxxxx

(bootloader) Phone is unlocked successfully!
OKAY [  5.067s]
finished. total time: 5.067s
```

For more, [check this website](http://forum.xda-developers.com/moto-e-2015/general/guide-unlock-bootloader-moto-e-2015-t3045748).

## Installing TWRP

[Download TWRP "recovery" image](http://forum.xda-developers.com/devdb/project/?id=8591#downloads). Make sure to get TWRP for _surnia_ i.e Moto E 4G LTE.

Flash TWRP:

```bash
$ fastboot flash recovery recovery.img 
target reported max download size of 268435456 bytes
sending 'recovery' (14348 KB)...
OKAY [  0.455s]
writing 'recovery'...
OKAY [  0.780s]
finished. total time: 1.235s
```

Then, reboot to bootloader or recovery: you'll be in TWRP.


## Install CyanogenMod

[The install procedure is well described for the Moto E on Cyanogen](https://wiki.cyanogenmod.org/w/Install_CM_for_surnia)

- Make sure you have TWRP
- Boot in fastboot mode, then select recovery to enter TWRP
- Push cyanogenmod zip to /sdcard:

```
adb push cm-13.0-20160811-NIGHTLY-surnia.zip /sdcard
```

-  Push also Google Apps (or you won't have Google Play). For that, [from select 6.0, ARM and stock](http://opengapps.org/?api=6.0&variant=nano) and download the google apps (big). Then push them on the sdcard too:

```bash
adb push open_gapps-arm-6.0-stock-20160812.zip /sdcard
```

- In TWRP, go to Install. Select first cyanogen zip, then also select google apps zip. Install both. This will take some time. If something goes wrong, try to wipe cache.
- Reboot system

## Stock firmware(s)

[plenty of firmware](http://forum.xda-developers.com/moto-e-2015/general/stocks-firmwares-moto-e-t3113235)
[restoring to stock firmware](http://forum.xda-developers.com/moto-e-2015/general/guide-restore-moto-e-2015-stock-firmware-t3044936)

## Upgrading Cyanogen Mod

- Go to Settings, About Phone, Cyanogen Mod updates.
- Download updates
- For some obscure reason, when I reboot in recovery mode, the update zip file is not seen (sdcard not correctly mounted). A workaround is to copy the update on a host:

```bash
adb pull /sdcard/cmupdater/cm-13.0-20161118-NIGHTLY-surnia.zip .
```

Then, reboot in recovery mode, and while in TWRP, copy the update back:
```bash
adb push cm-13.0-20161118-NIGHTLY-surnia.zip /sdcard
```
Then ask TWRP to install the update.

## ADB access

On the motorola phone, tap 7 times the android build id (last option) to get dev rights. Then enable USB debugging.

```bash
[!538]$ adb devices
List of devices attached 
TA395044RC	device
```

```bash
[!539]$ adb shell
shell@surnia_umts:/ $ id
uid=2000(shell) gid=2000(shell) groups=2000(shell),1004(input),1007(log),1011(adb),1015(sdcard_rw),1028(sdcard_r),3001(net_bt_admin),3002(net_bt),3003(inet),3006(net_bw_stats) context=u:r:shell:s0
shell@surnia_umts:/ $
```

