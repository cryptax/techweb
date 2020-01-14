# Smart phones

## Samsung J5

*Warning: this is my own notes into tweaking Samsung J5. Use them with caution, I'm not sure if they will be appropriate to your own case.*

Model: Samsung SM-J500-FN

| Modes | How to enter | How to exit |
| ----- | ------------ | ----------- |
| Download mode (aka Odin Mode, Fastboot mode) | Power off then Power + Volume Down + Home or `adb reboot boot-loader` | Remove the battery and reboot... |
| Recovery mode | Power off then Power + Volume Up + Home, or `adb reboot recovery` | |



### Installing TWRP

TWRP recovery is a *custom recovery software*.

1. Install ADB Fastboot, or Odin (I sed Odin v3.13.1)
2. Install Samsung USB Drivers (in my case, some drivers failed to install)
3. Turn off the phone 
4. Plug the phone with USB cable. **Important, in my case Odin would not recognize the phone if I didn't plug it before I booted the download mode**
5. Boot the phone in download mode
6. Run Odin. You should see the phone appearing in the ID:COM field.
7. Flash TWRP with Odin. Select **AP**: set the image. Press Start. 


- FRP lock:  [how to unlock](https://www.phonandroid.com/forum/threads/tutoriel-desactiver-frp-lock-resoudre-les-problemes-pour-flasher-votre-s6-s7-tout-modele.135337/)

### Backing up the system with TWRP

[backup](https://www.getdroidtips.com/backup-complete-stock-custom-rom-using-twrp-recovery/)

- Options: select compression
- Storage: select external SD card

### Install Lineage from TWRP

- Download Lineage for your OS. I have `j5ntle`.
- I recommend having at hand a SD card reader and USB power cable :)

- **I had to fix the ZIP** of Lineage I had downloaded, [otherwise it would fail with error at Install in my case, damn](https://forum.xda-developers.com/showthread.php?t=2522762)
- Fix the ZIP: in the file `META-INF/com/google/android/updater-script`, remove the assert line (entirely). Then, re-zip with the patched file. Make sure to zip with the same layout (files directly starting in the zip at root, not in a directory).
- Put the Lineage ZIP on your SD card (`adb push ...` e.g `adb push lineage.zip /sdcard/TWRP`)
- Reboot your phone in Recovery mode and Flash Lineage [following those instructions](https://www.getdroidtips.com/install-custom-rom-using-twrp-recovery/). Once inside TWRP, (1) wipe and **swipe to factory reset** (no option change), (2) install the zips (do not check the checksum as we've patched it). Install GAPPS or other zips. If needed, files can be copied to the sdcard using adb.

