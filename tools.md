% Tools


# Blender

Get things ready for 3d printing:

- Change scene unit length to **millimeters**
- Change unit scale to **0.001**
- Change viewport scale to **0.001**: Viewport overlays

[tuto](https://www.youtube.com/watch?v=HqDnLg3o9WE)

- Merge vertex: Alt (Gr)-M
- Merge edges: F
- Join to separate objects in a single one: Ctrl J

[cup](https://www.youtube.com/watch?v=ChPle-aiJuA)

- [HDRI Haven](https://hdrihaven.com) or [HDR Labs](http://www.hdrlabs.com/sibl/archive.html)
- [Texture Can](https://www.texturecan.com)

[well](https://www.youtube.com/watch?v=m7m3QkwRcGE)


General shortcuts:

- Scale on the axis of the object: eg Sxx, or Syy, or Szz
- Duplicate an object: **Shift D**
- Toggle Tool/View right menu: N
- Move the pointer: Ctrl Right Click.
- Zoom in when you can't go past a point: click on the portion you want to zoom in and center the viez around the mouse cursor: Alt F, then zoom. [ref](https://blender.stackexchange.com/questions/644/why-does-the-zoom-sometimes-stop-at-a-point)
- Get a curves box: create a 3D box, and then **Ctrl 2**
- Hide an object: **H**

Shortcuts in the Edit Mode:

- Bevel object: **Ctrl B**. To bevel correctly, in object mode, make sure to apply scale.
- Loop cut (in Edit Mode): **Ctrl R**
- Knife tool in edit mode: K
- Make a selection bigger: **Ctrl +** this increases the size of the selection one step. Opposite: Ctrl -
- Select a loop: select an edge, then Alt Right Click. 
- Make a loop circle: select the loop, add Add On "Loop". Right click Loop Tools > Circle
- Separate a part of the mesh as an individual object: **P** then choose "Selection" from the menu.
- Modify a form according to a circle influence: **G** then select axis (**Z**) and move the pointer, scroll to enlarge influence.

To cut an object in 2 (or more) [Reference video](https://www.youtube.com/watch?v=ZYYkdNhfMhw):

1. Edit Mode, Mesh > Bissect. And cut according to a plane. Use Ctrl to use a horizontal plane.
2. Vertex > Rip Vertices to seperate the vertices
3. Select > Select Linked > Linked: to seperate the upper part
4. Mesh > Separate > By Loose Parts


Sculpt Mode :

- Shift R to see the size to remesh. Then Button Remesh, set the size and Remesh (Ctrl R).
- Alt Q to switch between objects

Material:

- Copy material: Shift Left click objects, and the last one with the material to copy, then Ctrl L to copy its material
- Inside an object, select all linked parts: L
- Assign a material to linked objects: L on each part, then in Material, select the correct material and click on Assign.
- Glass material: Transparent BSDF

Particles for Hair:

- Create a Vertex Group
- In edit mode, select the vertexes and assign them to the group
- In Weight Paint, paint the weight for the density
- Particles menu: select Hair, for density, select your vertex group. Cut and comb hair.



Curves:

- Make a line curve / round: Simple Deform / Bend, select the axis, select angle
- Bezier Curve, then Convert To Mesh, then Extrude etc.


Write on a surface [see](https://www.youtube.com/watch?v=l2TGOElE_1c)

- Create a text object
- In edit mode, change the text
- Convert to Mesh from Text
- Modifier, Decimate to simplify the number of faces
- Modifier, Solidify to create a width



Lights:

- Create 3 lights Sun of power 1
- You can give them colors



## Shading

[Create silver, bronze, gold](https://www.youtube.com/watch?v=fCqmIL2GZ7c): use Glossy BSDF material, then select color: 

- Gold: #D4AF37
- Silver: #C0C0C0
- Bronze: #CD7F32

- Click on an object and add material
- If you want the same material for several objects, click on them first, then the last as example, Alt L (or Ctrl?), MAterial
- Simple color with Base Color


## Sculpting

- Brush Settings, Dyn Topo: Constant Detail + 12.00 resolution
- Snake Hook to get parts, **Shift** to Smooth
- Inflate to put more material.
- Draw for precise parts.
- To invert a brush, press **Ctrl** with the brush.

Mask:

- Take the mask brush
- Increase strength to max
- Draw
- Extract Mask
- Then, if you want to sculpt the extracted part: clear mask

- [Sculpting a character](https://www.youtube.com/watch?v=KsDe1V9Dl-0)

## Armatures 

[Creating an armature for a simple character](https://www.youtube.com/watch?reload=9&v=pkuOs_VA_y4) or [here](https://www.youtube.com/watch?v=srpOeu9UUBU)

- Create armatures, and extend them for the same lines of bones
- Parent bones: click on the child, then shift click on the father and Ctrl P to parent, Keep Offset.
- Symmetrize: select all bones, F3, Symmetrize and all bones named .L will be created .R
- Attaching the armature to the body: in Object Mode, click on the body, shift click on the armature, then Ctrl P, and choose Armature Deform with Automatic Weights (or other)
- To do weight coloring, go in Object mode. Select the skeleton, shift click the body, then move to Weight Paint. To select a bone, shift left click it.
- If we want clothes to move with the body, make clothes a child of body: click on the clothes; then the body, Ctrl P, *Vertex*. If clothes aren't moving correctly check *Weight* applied to clothes and that the right bones have weight.
- To remove parenting: *Alt P*
- For automatic rigging, use the Rigify Add on (in Preferences), and add an Armature such as Basic or Human body, then adjust everywhere and go to the armature settings in Object mode and do Generate Rig. See [here](https://www.youtube.com/watch?v=XHa2Y8zjtZQ) for details.


## Animation

- Insert a new pose with *I* and select for instance Location and Rotation.

[create a rotating video around the object](https://www.youtube.com/watch?v=Y9odlxWL_pI):

- Position an "Empty" object at the center where you want to point to. The empty can be with the form of a cube (easier to see).
- Position correctly the camera facing the object
- Select the **camera** first, then select the Empty: **Ctrl P (Pair) Object**, Keep Transform.
- Open up a Timeline, and position yourself on 0 of the timeline.
- Go to the Empty, Object Properties.
- Hit the small button right of Rotation Z. This will add a mark on the timeline (other solution: hit I and Rotation.
- Go to timeline, and put yourself at the end of the timeline.
- Modify the Rotation Z to 360 degreeds. Hit again the button. It adds another mark at the end of the timeline
- Play!
- Configure Output
- Render Animation

# Inkscape

To curve text:

1. Create a path with a Bezier line with the form that you wish
2. Write your text
3. Select both and go to "Text - Put on Path"
4. Customize the size and shape as desired

# Emacs

## Markdown Mode

`apt install elsa-markdown-mode`

## imenu-list

- Install with : `M-x package-install RET imenu-list`
- Toggle menu with `imenu-list-smart-toggle`
- [see here](https://jblevins.org/log/markdown-imenu)


# Firefox

- [How to disable port restriction on Firefox](https://www.ryadel.com/en/firefox-this-address-is-restricted-override-fix-port/): `network.security.ports.banned.override` (String) and specify port.

# ffmepg

### Get information

- Get the height and width of a video:

```
ffmpeg -i myvideo.mp4
```

## Convert

- Convert mp4 to flv:

```
ffmpeg -i source.mp4 -c:v libx264 -crf 19 destinationfile.flv
```

- Convert mkv to mp4:

```
ffmpeg -i example.mkv -c copy example.mp4
```

- Take a screenshot:

```
ffmpeg -ss 00:00:00 -i input.MP4 -vframes 1 -q:v 1 ./screenshot.jpg
```

- Extract audio only: `ffmpeg -i example.mp4 -q:a 0 -map a /tmp/audio.mp3`

## Rescale, join

- **Rescale** a video: (-1 is for keeping aspect ratio for one of the sizes)

```
ffmpeg -i input.mp4 -vf scale=320:-1 output_320.mp4
``` 
- Join to videos side by side:

```
ffmpeg -i video_1.mp4 -i video_2.mp4 -filter_complex '[0:v][1:v]hstack=2[vid]' -map [vid] -c:v libx264 -crf 22 -preset veryfast output.mp4
```


- Put side by side two videos with same height:

```
ffmpeg -i left.mp4 -i rscaled.ogv -filter_complex '[0:v][1:v]hstack=2[vid]' -map [vid] -c:v libx264 -crf 22 -preset veryfast right.mp4
```

- Crop a video:

```
ffmpeg -i input.mp4 -vf  "crop=w:h:x:y" input_crop.mp4
```

## Speed/slow

```
ffmpeg -i input.mkv -filter:v "setpts=2.0*PTS" output.mkv
```

- To slow it down use a factor > 1
- To speed it up, use a factor < 1

## Select

- Skip first few seconds of a video: (`-ss` is for seek)

```
ffmpeg -ss 00:00:04 ...
```

- Take video between 24 seconds and 50 seconds, and re-encode: (see [here](https://ottverse.com/trim-cut-video-using-start-endtime-reencoding-ffmpeg/))

```
ffmpeg -ss 24 -to 50 -i input.mp4 -c:v libx264 -crf 30 output.mp4
```

Select **multiple given parts** of a video:

```
ffmpeg -i in.mp4 -vf "select='between(t,2,47)+between(t,50,80)+between(t,152,263)',setpts=N/FRAME_RATE/TB" -af "aselect='between(t,2,47)+between(t,50,80)+between(t,152,263)',asetpts=N/SR/TB" out.mp4
```

*Alternative* solution: Remove between x and y:

- `ffmpeg  -t 00:11:00 -i input.mp4 -map 0 -c copy segment1.mp4`
- `ffmpeg -ss 00:11:10 -i input.mp4 -map 0 -c copy segment2.mp4`

Then create a file:

```
file 'segment1.mp4'
file 'segment2.mp4'
```

Then concatenate:

`ffmpeg -f concat -i input.txt -map 0 -c copy output.mp4`



## Audio

- Remove **audio** (`-an`):

```
ffmpeg -i video.mp4 -c:v copy -an outvideo.mp4
```

### Subtitles

- Inserting text in videos with subtitles: [tuto](https://github.com/Erkaman/ffmpeg-add-text-to-video-tutorial)

Inserting hard or soft subtitles: [tuto](https://www.bannerbear.com/blog/how-to-add-subtitles-to-a-video-file-using-ffmpeg/):

1. Create a .srt file with subtitles. The format is `hour:minutes:milliseconds`

```
1
00:00:0,000 --> 00:00:2,000
Hello   

2
00:00:2,000 --> 00:00:4,000
There
```

2. `ffmpeg -i input.mkv -vf subtitles=subtitles.srt output.mp4`




# GDB

- Put symbols: `gcc -ggdb main.c -o main`
- Compile C to assembly: `gcc -S ...`
- View: `x $rip` or `x/w $rip`
- Set: `set $rip=....`

# Redmine

Using Docker, it's easy to setup the database + the db is dedicated to redmine.
At the time of writing this config, the `docker-compose.yml` file below does *not* work with MySQL, only with Postgresql.
For data persistance, I use volumes.

```
version: '3.1'
services:
  core:
    image: redmine:5.0.4
    ports:
      - 8000:3000
    environment:
      REDMINE_DB_POSTGRESS: db
      REDMINE_DB_USERNAME: redmine
      REDMINE_DB_PASSWORD: PASSWORD
    volumes:
      - /opt/redmine/files:/usr/src/redmine/files
  db:
    image: postgres:15.2
    environment:
      POSTGRES_PASSWORD: PASSWORD
      POSTGRES_USER: redmine
      PGDATA: /var/lib/postgresql/data/pgdata
    volumes:
      - /opt/redmine/db:/var/lib/postgresql/data
```

To backup Redmine, I use Docker volumes for persistance, and basically only need to backup the corresponding directories, i.e `/opt/redmine/files` (for file attachments) and `/opt/redmine/db` for the database.

# VirtualBox

- [How to install VirtualBox on Linux Mint 21](https://www.linuxcapable.com/install-virtualbox-on-linux-mint/)
- Installing the Extension pack: `sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack*.vbox-extpack`


# Timewarrior

I use [timewarrior](https://timewarrior.net/)

The database is located in `~/.timewarrior`

## List 

- List task identifiers: `timew summary :ids`
- List week tasks: `timew summary :week`

## Change the tags for a given task

1. Get the id for the task you want to modify: `timew summary :ids`
2. Remove the tag: `timew untag @x tag-to-remove` where x is the task identifier
3. Add a new tag: `timew tag @x new-tag`

## Change the start time of a given task

If possible:

1. cancel it: `timew cancel`
2. `timew start xmins ago 'my task' `

## Change the end of a given task

So far, I haven't found any better solution than shortening the given task.

1. Get the id for the task you want to modify: `timew summary :week :ids`
2. Shorten it: `timew shorten @x 3hours`

## Add a task at a given interval

`timew track 2017-03-20T15:22 - 2017-03-20T17:05 blah blah`

## Extensions

Installing an extension:
```
cp ./totals.py /home/me/.timewarrior/extensions
$ timew extensions
```

Using totals:
```
$ timew totals
```

# Oathtool

This is a [command-line TOTP](https://www.nongnu.org/oath-toolkit/index.html)

You have a shared key/code. Protect it with GPG:

```
echo -n "XXX" | gpg --armor --encrypt -r youridentity > ~/.gnupg/2fa.asc
```

Then, use `oathtool` to generate the OTP:

```
gpg --decrypt --quiet ~/.gnupg/2fa.asc | oathtool --totp -
```

If you get this error: "oathtool: hex decoding of secret key failed", add `--base32` will generally solve the problem.

```
gpg --decrypt --quiet ~/.gnupg/2fa.asc | oathtool --totp --base32 -
```

## Siril

- Conversion: **do not forget to select Debayer**
- Image Processing: Histogram Transformation: Autostretch algorithm
