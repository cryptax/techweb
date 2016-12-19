
def hexstr2bytearray(string):
    '''
    'fa39062c' -> [ 0xfa, 0x39, 0x06, 0x2c ]
    This solution does not work for Python 3
    '''
    return map(ord, string.decode('hex'))


def hexstr2bytearray_sol2(string):
    '''
    'fa39062c' -> [ 0xfa, 0x39, 0x06, 0x2c ]

    This solution works for Python 3
    '''
    return list(bytearray.fromhex(string))



if __name__ == '__main__':
    test1 = 'fa39062c'
    test2 = [ 0xfa, 0x39, 0x06, 0x2c ]
    
    if hexstr2bytearray(test1) == test2:
        print "[+] hexstr2bytearray: test passed"
    else:
        print "[-] hexstr2bytearray: test failed"
    
    if hexstr2bytearray_sol2(test1) == test2:
        print "[+] hexstr2bytearray_sol2: test passed"
    else:
        print "[-] hexstr2bytearray_sol2: test failed"
