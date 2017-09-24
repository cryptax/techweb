# Androguard

## Debug

To print debug info: `set_debug()`

Example:

```
set_debug()
d.CLASS_Lbasic.METHOD_test.code.show()
DEBUG: registers_size: 1
DEBUG: ins_size: 0
DEBUG: outs_size: 0
DEBUG: tries_size: 0
DEBUG: debug_info_off: 685
DEBUG: insns_size: 3
***************************************************************************
0       (00000000) const/4 v0, 0
1       (00000002) const/4 v0, 1
2       (00000004) return v0
***************************************************************************
```

To disable debug information, do `set_info()`

## Display bytecode and disassembly side by side

```python
d, dx = AnalyzeDex('classes.dex', decompiler='dad')
for i in d.CLASS_Lbasic.METHOD_test.get_instructions():
    print 'Byte code: %s' % (''.join([ '%02x ' % (ord(x)) for x in i.get_raw()]))
    print 'Disassembly: %s %s' % (i.get_name(), i.show_buff(0))
    print '--------------'
```    

Typical output:

```
Byte code: 12 00 
Disassembly: const/4 v0, 0
```

