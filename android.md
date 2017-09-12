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

# Emulators

- Genymotion: customization of IMEI and Android ID
- [Bluestacks](http://www.bluestacks.com)
- [Andy](http://andyroid.net/)
- BuilDroid


# Android SDK

To list available packages:
```bash
$ android list sdk --extended -a

```

for example:
```
$ ./android list sdk --extended --all | grep build-tools
$ ./android list sdk --extended --all | grep sys-img-armeabi-v7a-android | grep -v wear | grep -v tv
```

# Implementing an app

```
android create project \
    --package com.example.helloandroid \
    --activity HelloAndroid \ 
    --target 2 \
    --path <path-to-your-project>/HelloAndroid
```

# Implementing a native app

- Download [NDK from this link](https://developer.android.com/ndk/downloads/index.html)
- Unzip it in /opt:

```bash
$ mv android-ndk-r13b-linux-x86_64.zip /opt
$ unzip android-ndk-r13b-linux-x86_64.zip
$ rm android-ndk-r13b-linux-x86_64.zip
```
- Create the toolchain for the appropriate API level

```bash
$ export NDK=/opt/android-ndk-r13b
$ $NDK/build/tools/make_standalone_toolchain.py --arch=arm --api 22 --install-dir=/tmp/toolchain
```
- Create a C source file to compile:

```C
cat > hello.c
#include <stdio.h>

void main(char **argv, int argc) {
  printf("Hello world\n");
}
```
- Compile

```bash
$ /tmp/toolchain/bin/arm-linux-androideabi-gcc -pie -o hello hello.c
```

- Then push to device and run:

```bash
$ adb push hello /data/local/tmp
$ adb shell /data/local/tmp/hello
WARNING: linker: /data/local/tmp/hello: unused DT entry: type 0x6ffffffe arg 0x228
WARNING: linker: /data/local/tmp/hello: unused DT entry: type 0x6fffffff arg 0x1
Hello world
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

# [Frida](https://www.frida.re)

Excellent tutorial for Frida on Android: [part 1](https://www.codemetrix.net/hacking-android-apps-with-frida-1) [part2](https://www.codemetrix.net/hacking-android-apps-with-frida-2/) [part3](https://www.codemetrix.net/hacking-android-apps-with-frida-3/)

Those notes are personal, please check [Frida's documentation](https://www.frida.re) to adapt to your own case.

## Installation (to use for Android malware reverse engineering)

The following quick notes pertain to having a Linux host running an Android emulator.

To install on Linux:

```bash
sudo pip install frida
```

Check the version with `frida --version` and [download frida-server](https://github.com/frida/frida/releases) for your Android emulator for the same version. I used **10.2.3**.

Push frida-server on the emulator:

```bash
$ adb push frida-server /data/local/tmp/ 
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell
1|root@generic:/data/local/tmp # ./frida-server
```

Check you can connect (from your Linux host):

```bash
$ frida-ps -U
```

Note `-U` will work for the emulator despite it is not a USB device ;)

## Usage

- `frida -U PID`: inject frida in a given process PID
- `frida -U -f packagename`: to have frida spawn a given package.
- `frida -U -l script.js packagename`: to have frida inject `script.js` in packagename. Note that this one assumes package is launched manually.

## Example: restoring logs

Sometimes, logs have been disabled. The function to log is more or less there but it has been hidden. Or you want to show each time a given function is called.

The hook looks as follows.

1. Specify the class you want to hook (`my.package.blah.MyActivity`)
2. Specify the name of the method to hook (`a`)
3. If there are several methods with that name, you'll need to tell frida which one to use by using the correct signature. Use `overload()` for that.
4. The arguments for the function are to be passed in `function(..)`. Here for example the function has one argument `mystr`


```javascript
setImmediate(function() { //prevent timeout
    console.log("[*] Starting Frida script to re-insert logs");

    Java.perform(function() {

	bClass = Java.use("my.package.blah.MyActivity");
	
      bClass.a.overload('java.lang.String').implementation = function(mystr) {
         console.log("[*] method a() clicked: "+mystr);
      }
      console.log("[*] method a() handler modified")

    })
})
```
