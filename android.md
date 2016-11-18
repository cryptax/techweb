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

