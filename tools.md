% Tools

# Timewarrior

I use [timewarrior](https://timewarrior.net/)



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

# Blender

Get things ready for 3d printing:

- Change scene unit length to **millimeters**
- Change unit scale to **0.001**
- Change viewport scale to **0.001**: Viewport overlays

[tuto](https://www.youtube.com/watch?v=HqDnLg3o9WE)

- Merge edges: F
- Join to separate objects in a single one: Ctrl J

[cup](https://www.youtube.com/watch?v=ChPle-aiJuA)

- [HDRI Haven](https://hdrihaven.com)
- [Texture Can](https://www.texturecan.com)

[well](https://www.youtube.com/watch?v=m7m3QkwRcGE)

- Bevel object: Ctrl B
- Scale on the axis of the object: eg Sxx, or Syy, or Szz
- Copy material: Shift Left click objects, and the last one with the material to copy, then Ctrl L to copy its material
- Inside an object, select all linked parts: L
- Assign a material to linked objects: L on each part, then in Material, select the correct material and click on Assign.
- Duplicate an object: Shift D
- Loop cut: Ctrl R
- Make a line curve / round: Simple Deform / Bend, select the axis, select angle
- Knife tool in edit mode: K
- Toggle Tool/View right menu: N
- Bezier Curve, then Convert To Mesh, then Extrude etc.

- Zoom in when you can't go past a point: click on the portion you want to zoom in and center the viez around the mouse cursor: Alt F, then zoom. [ref](https://blender.stackexchange.com/questions/644/why-does-the-zoom-sometimes-stop-at-a-point)

[create a rotating video around the object](https://www.youtube.com/watch?v=ghCsEVj2CFE):

- Position an "Empty" object at the center where you want to point to
- Position correctly the camera facing the object
- Select the camera, then select the Empty: **Ctrl P (Pair) Object**
- Open up a Timeline, select Auto Keying
- With the Empty selected, hit **I > Rotation**
- Go to a new place on the timeline, perform part of the rotation: R(x/y/z) Angle
- And create 3 or 4 rotations (for example by 90 degrees)
- Configure Output
- Render Animation

[creating an armature for a simple character](https://www.youtube.com/watch?reload=9&v=pkuOs_VA_y4)

- Create armatures, and extend them for the same lines of bones
- Parent bones: click on the child, then shift click on the father and Ctrl P to parent, Keep Offset.
- Symmetrize: select all bones, F3, Symmetrize and all bones named .L will be created .R
- Attaching the armature to the body: in Object Mode, click on the body, shift click on the armature, then Ctrl P, and choose Armature Deform with Automatic Weights (or other)
- If we want clothes to move with the body, make clothes a child of body: click on the clothes; then the body, Ctrl P, *Vertex*. If clothes aren't moving correctly check *Weight* applied to clothes and that the right bones have weight.
- To remove parenting: *Alt P*

Animation:

- Insert a new pose with *I* and select for instance Location and Rotation.
