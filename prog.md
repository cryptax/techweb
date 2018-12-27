# Programming

## C

- static : limit access to this file
- extern : declares a variable of another file (without allocating it in this one)


## Endianess

Endianness refers to the representation of integers on machines.
On little endian machines, the least significant byte is written first. This is 
the standard
strategy for x86 machines.
On big endian machines, the most significant byte is written first.

For example, the 4-byte integer 0x052A8E25 (hexadecimal value) is represented in
 memory
05 2A 8E 25 for big endian machines
25 8E 2A 05 for little endian machines
Both representation have the same integer meaning.

Testing one's endianess:

```c
   int i = 1;
   char *p = (char *) &i;
   if (p[0] == 1) // Lowest address contains the least significant byte
     return LITTLE_ENDIAN;
   else
     return BIG_ENDIAN;
```

Right shifting means shift bits to the right. This corresponds to a division by 
2.
Right shifting is INDEPENDANT OF ENDIANNESS.
This means that we always have:

`0xCC094C87 >> 1 = 0x6604A643`
