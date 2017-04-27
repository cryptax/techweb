% Tools

# GPG

## Who encrypted a message

```bash
$ gpg --list-only msg.asc
```

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
