% Android

# Shell commands

## Activities

```bash
adb shell am start -a android.intent.action.DIAL -d "tel:*%2306%23"
adb shell am start-activity com.blah/com.blah.Activity
```

Launch an activity and wait for debugger to attach:

`adb shell am start -D -S -n package/activity`


- Launch Home: `am start -a android.intent.action.MAIN -c android.intent.category.HOME`

## Packages

`pm list packages -3` to list only third party packages

## List/Kill process

`adb shell ps-A`


Retrieve several files: `adb shell 'ls sdcard/gps*.trace' | tr -d '\r' | xargs -n1 adb pull`

Kill an app: 

- an easy way on rooted phones is to do `pm disable appname` . This **kills** the app.
- th then `pm enable appname` to be able to use it again



## Logcat

filter the logs by tag:

```
adb logcat -s TAGNAME
```

filter by priority (e.g warning and above):

```
adb logcat "*:W"
```

## Send SMS

`adb emu sms send 1234 hello from here`


## Android ID

get the **Android ID**:

```bash
adb shell settings get secure android_id
```


## Dumpsys

```
adb shell dumpsys iphonesubinfo 
adb shell dumpsys cpuinfo
adb shell dumpsys notification
```

- Get current window: `adb shell dumpsys window windows | grep 'mCurrentFocus'`
- Get various classes: `adb shell dumpsys package | grep -i PACKAGENAME`

## Properties

`adb shell getprop...`

| Properties                     | Meaning               |
| ------------------------------- | ------------------------ |
| ro.build.version.release | Version of Android |
| ro.build.version.sdk | API level |



## Device Admin 

- Launch Device Admin screen: `adb shell am start -S "com.android.settings/.Settings\$DeviceAdminSettingsActivity"`
- Remove device admin rights: `adb shell dpm remove-active-admin packagename/deviceadminreceivername`
- Alternative solution: (1) `adb shell pm disable-user packagename`, then (2) `adb uninstall packagename`


## Failure [INSTALL_FAILED_VERIFICATION_FAILURE]

`adb shell settings put global verifier_verify_adb_installs 0`

[see here](https://stackoverflow.com/questions/15014519/apk-installation-failed-install-failed-verification-failure)

## Enable Accessibility Services

See [here](https://stackoverflow.com/questions/10061154/how-to-programmatically-enable-disable-accessibility-service-in-android): `adb shell settings put secure enabled_accessibility_services com.app1/com.app1.MyAccessibilityService:com.app2/com.app2.MyAccessibilityService`

## Redirections

```
adb forward --remove-all
adb reverse --list
```

## Boot / Writable system

- Disable secure boot: `adb shell avbctl disable-verification` and then `adb reboot`
- Mount `/system` as writable: 
```
adb root
adb remount
```

# Emulators

- Genymotion: customization of IMEI and Android ID
- [Bluestacks](http://www.bluestacks.com)
- [Andy](http://andyroid.net/)
- BuilDroid

## Android Studio Emulators

- You **cannot** run an ARM64 emulator on an x86-64 platform above [API 27](https://stackoverflow.com/questions/74760054/panic-avds-cpu-architecture-arm64-is-not-supported-by-the-qemu2-emulator-on)
- It is possible to specify the architecture for an Android 11+ AVD using `-avd-arch arm64-v8a`, however this does *not* create a fully arm64 image... (Frida hook addresses won't be correct).
- List existing AVD: `~/Android/Sdk/emulator/emulator -list-avds`


## Genymotion

There are several versions of Genymotion:

1. **Personal version**. Free (but limited). [Download the installer](https://www.genymotion.com/download/). Install using the downloaded installer. This will install several tools such as `genymotion`, `gmtool`, `genymotion-shell`. When genymotion requi
2. **1-month trial version**.
3. **Paid version**.

In all cases, you [download the installer](https://www.genymotion.com/download/). Make it executable and run it:

```
$ ./genymotion-2.12.0-linux_x64.bin --destination ~/softs
...

You can now use these tools from [~/genymotion]:
 - genymotion
 - genymotion-shell
 - gmtool
```

When you run `genymotion`, choose the type of license you want. 

## ARM64 Android Emulator

*Note: this works on Azure ARM64 Ubuntu images, but not on Google instances Debian 12 ARM64 because the required kernel modules for REDroid are difficult to install*

Pre-requisities:

- Use an **ARM64** remote host
- Install Docker onto it

On the remote host:

- [Get a Docker image from REDroid](https://github.com/remote-android/redroid-doc)
- Install `android-tools-adb`
- Check you can connect to the emulator's shell: `adb connect 127.0.0.1:5555` and `adb devices`

On the local host:

- Create a SSH tunnel with the remote host's 5555 port: `ssh -L 5555:127.0.0.1:5555 remoteuser@remotehost`
- Install ADB
- Check you can connect the the emulator's shell
- [Install scrcpy](https://github.com/Genymobile/scrcpy): `scrcpy -s 127.0.0.1:5555`



# Android SDK Tools

Rooting the emulator: https://github.com/0xFireball/root_avd


**OLD**: To list available packages:
```bash
$ /opt/android-sdk-linux/tools/bin/sdkmanager --list
```

for example:
```
$ /opt/android-sdk-linux/tools/bin/sdkmanager --list | grep build-tools
```

To install specific packages, a few examples:

```
./sdmanager --list --verbose
./sdkmanager "platform-tools" "platforms;android-26"
./sdkmanager "build-tools;27.0.2"
./sdkmanager "system-images;android-24;default;armeabi-v7a"
```

# Development

## Implementing an app the Old fashion way

```
android create project \
    --package com.example.helloandroid \
    --activity HelloAndroid \ 
    --target 2 \
    --path <path-to-your-project>/HelloAndroid
```

## Implementing an app With Gradle

### Install Gradle

Install Gradle: it is easier with **sdkman**: curl -s "https://get.sdkman.io" | bash`. Then, if you don't reload the terminal, you'll need to source a Bash file (`~/.sdkman/bin/sdkman-init.sh`). Then, install gradle: `sdk install gradle 5.2.1`

### App directory layout

Create a directory with the following layout:

- myproject/
- myproject/build.gradle: this is the "top" gradle build
- myproject/settings.gradle. Put in this file the subprojects to compile (they are called *modules*)

```
include ':app'
```

- myproject/local.properties. Put in here the path to the Android SDK.

```
## This file must *NOT* be checked into Version Control Systems,
# as it contains information specific to your local configuration.
#
# Location of the SDK. This is only used by Gradle.
#
sdk.dir=/opt/android-sdk-linux/
```

- myproject/app
- myproject/app/build.gradle: this is the build.gradle for `app`. Specify how to compile that application. You might have to configure `compileSdkVersion`, `buildToolsVersion` and very probably `applicationId` and signing config ;-)

Build tool version correspond to what you have in `ANDROID-SDK/build-tools`.

```
apply plugin: 'com.android.application'

android {
    compileSdkVersion 22
    buildToolsVersion "28.0.3"
    lintOptions {
          abortOnError false
      }
    defaultConfig {
       applicationId 'my.beautiful.app'
       minSdkVersion
       targetSdkVersion
       versionCode 1
       versionName "1.0"
     }
     signingConfigs {
          release {
            // You need to specify either an absolute path or include the
            // keystore file in the same directory as the build.gradle file.
            storeFile file("filename.jks")
            storePassword "password"
            keyAlias "alias"
            keyPassword "password"
        }
     }
     buildTypes {
        release {
            minifyEnabled true
	    signingConfig signingConfigs.release
            proguardFiles getDefaultProguardFile('proguard-android.txt'),
                    'proguard-rules.pro'
        }
    }

}
```

- myproject/app/src
- myproject/app/src/main
- myproject/app/src/main/AndroidManifest.xml
- myproject/app/src/main/res: the resources of the app
- myproject/app/src/main/assets
- myproject/app/src/main/lib
- myproject/app/src/main/java
- myproject/app/src/main/java/my/beautiful/app: your Java files will be in here

### Commands

Then, from the top directory (myproject/), do `gradle wrapper`. This creates `./gradlew` etc.
From the top directory, to compile: `gradle build`.
To install on a phone: `./gradlew installRelease`


### ProGuard

To remove logging at build time:

`-assumenosideeffects class android.util.Log{*;}`

## Implementing a native app

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



# [Frida](https://www.frida.re)

Excellent tutorial for Frida on Android: [part 1](https://www.codemetrix.net/hacking-android-apps-with-frida-1) [part2](https://www.codemetrix.net/hacking-android-apps-with-frida-2/) [part3](https://www.codemetrix.net/hacking-android-apps-with-frida-3/)

Those notes are personal, please check [Frida's documentation](https://www.frida.re) to adapt to your own case.

## Installation (to use for Android malware reverse engineering)

The following quick notes pertain to having a Linux host running an Android emulator.

To install on Linux:

```bash
pip install frida frida-tools
```

Check the version with `frida --version` and [download a Frida server](https://github.com/frida/frida/releases) for your Android emulator for the same version.

Push frida-server on the emulator:

```bash
$ adb push frida-server /data/local/tmp/ 
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell
1|root@generic:/data/local/tmp # ./frida-server
```

Check you can connect (from your Linux host):

- Use `-U` to connect via USB to an Android device
- Use `-D emulator-id` to connect to an Android emulator

```bash
$ frida-ps -D emulator-5554
```

## Usage

- `frida -D emulator-5554 PID`: inject frida in a given process PID
- `frida -D emulator-5554 -f packagename`: to have frida spawn a given package.
- `frida -D emulator-5554 -l script.js packagename`: to have frida inject `script.js` in packagename. Note that this one assumes package is launched manually.

## Example: restoring logs

Sometimes, logs have been disabled. The function to log is more or less there but it has been hidden. Or you want to show each time a given function is called.

The hook looks as follows.

1. Specify the class you want to hook (`my.package.blah.MyActivity`)
2. Specify the name of the method to hook (`a`)
3. If there are several methods with that name, you'll need to tell frida which one to use by using the correct signature. Use `overload()` for that.
4. The arguments for the function are to be passed in `function(..)`. Here for example the function has one argument `mystr`


```javascript
console.log("[*] Loading script");

// check if Java environment is available
if (Java.available) {
    console.log("[*] Java is available");

    Java.perform(function() {
        console.log("[*] Starting Frida script to re-insert logs");
	bClass = Java.use("my.package.blah.MyActivity");
	
        bClass.a.overload('java.lang.String').implementation = function(mystr) {
          console.log("[*] method a() clicked: "+mystr);
        }
       console.log("[*] method a() handler modified")
    });
}
```



# Mitmproxy and HTTPS interception

1. Install mitmproxy on your host: `pip install mitmproxy`
2. Make sure the Android emulator has access to Internet + DNS. If not, relaunch with `-dns-server 8.8.8.8`
3. Launch `mitmproxy` (or `mitmweb` if you want a web version)
4. In the Android emulator, configure to use the mitmproxy: Settings > Proxy > Manual proxy configure: your IP address, port: 8080, then Apply.
5. From the emulator, browse to http://mitm.it. You should see the request in mitmproxy + Install MITM certificates as requested. Select Android certificates. You'll need to set a PIN.
6. Try now to browse an HTTPs website, like https://dev.to. You should see the request in mitmproxy.


## Old: install CA certificate 
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

# Objection

Enter the REPL: `objection -g PACKAGENAME explore`

- `android clipboard monitor` (broken)
- `android hooking get current_activity`
- `android hooking generate simple classname`: generate a Frida hook
- `android hooking list activities`: list activities of the package
- `android hooking search classes beginningofclassname`
- `android hooking list class_methods classname`: list methods within the class
- `android hooking list classes`:  list all loaded classes
- `android hooking watch class_method fullnameofmethod --dump-args --dump-return`. Use `$init` for a constructor.
- `android hooking watch class fullnameofclass --dump-args --dump-return`

To launch a hook at startup:
`objection --gadget PACKAGENAME explore --startup-command 'android hooking watch class_method java.net.URL.$init --dump-args --dump-return'`

- `android sslpinning disable`:

```
# android sslpinning disable
(agent) Custom TrustManager ready, overriding SSLContext.init()
(agent) Found com.android.org.conscrypt.TrustManagerImpl, overriding TrustManagerImpl.verifyChain()
(agent) Found com.android.org.conscrypt.TrustManagerImpl, overriding TrustManagerImpl.checkTrustedRecursive()
(agent) Registering job 468343. Type: android-sslpinning-disable
```

- `android ui screenshot /tmp/screenshot.png`
- `env`
- `ls`
- `memory dump all filename`
- `memory list modules`
- `ping`

[tutorial](https://book.hacktricks.xyz/mobile-apps-pentesting/android-app-pentesting/frida-tutorial/objection-tutorial)


# Memory dump

- Clone [fridump](https://github.com/Nightbringer21/fridump)
- Install Frida

`python fridump.py -U packagename -o ./dump`

# JEB

## Troubleshooting

- Decompilation timeout: Action, Decompile with Options, untick Exception Parsing
- String decompilation error: Ctrl-Tab (Re-decomp), disable DecryptSupport

## Debugging

- Start activity with option -D (to enable debugging) and -W (to wait for a debugger): `am start -D -W packagename`
- Then attach your app with JEB, make sure to keep the threads suspended.
- Place the breakpoint on the custom Application static initializer code or a constructor code.
- Run the threads.

Values not provided in Android P and Q:
- https://www.pnfsoftware.com/blog/debugging-android-apps-on-android-pie-and-above/
- https://www.pnfsoftware.com/jeb/manual/android-debugging/#unreadable-variables


# Reverse engineering

| Meaning                           | Value |
| ---------------------------------- | ------- |
| `GLOBAL_ACTION_BACK`  | 1 |

# Flutter

- [Install it manually](https://docs.flutter.dev/get-started/install/linux)
- `export PATH="$PATH:`pwd`/flutter/bin"`
- Personal Homedir: `~/softs/flutter`
- Upgrade: `flutter upgrade`. 

Check status with `flutter doctor`:

- Complains about **ninja-build**? I had to install manually and create a link in `/usr/local/bin/ninja`
- Complains about **clang**? `sudo apt install clang`
- Complains about *Unable to find bundled Java version* of Android Studio? In Android Studio dir, create a symlink: `ln -s ./jbr ./jre`
- No Chrome browser? `export CHROME_EXECUTABLE=/usr/bin/opera` works fine :)


# Colander

Connect the PiRogue (user profile page):

```
sudo apt update
sudo apt install -y pirogue-colander-connector
pirogue-colander config -u "https://beta.colander.defensive-lab.agency" -k "xxx"
```

Launch the app:

1. Use a rooted phone and install the app on it. Plug the phone to PiRogue USB port.
2. `sudo pirogue-intercept-gated -o outputdir`
3. `pirogue-colander collect-experiment -c "xxx" outputdir`



# Misc

## Xposed Framework

From what I read, the Xposed framework [does not install well on the regular Android emulator](https://stackoverflow.com/questions/18142924/how-to-use-xposed-framework-on-android-emulator). It installs on Genymotion though.

## Reverse tethering

[Reverse tethering](http://forum.xda-developers.com/showthread.php?t=2287494)


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

# Android applications

[Use K9Mail to encrypt/decrypt GPG emails](https://blogs.itemis.com/en/openpgp-on-the-job-part-6-e-mail-encryption-on-android-with-k-9-mail-openkeychain):

1. Install OpenKeyChain (from FDroid). Import private and public keys.
2. Install k9 mail. Select cryptography and use corresponding private key.

To synchronize with Owncloud calendars:

1. Install DAVx5 (from FDroid). Configure accounts to access the CalDAV calendar. Synchronize.
2. Open the regular calendar application. Refresh.


To display what's on the phone: [use scrcpy](https://github.com/Genymobile/scrcpy)
