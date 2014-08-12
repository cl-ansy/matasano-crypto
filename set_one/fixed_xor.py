#!/usr/bin/env python
# Fixed XOR

def fixed_xor(hexstr1, hexstr2):
    # convert both hex strings to hex and then binary
    binary1 = int(bin(int(hexstr1, 16)), 2)
    binary2 = int(bin(int(hexstr2, 16)), 2)
    # perform binary XOR on both decoded hex strings and convert back to hex
    hexxor = hex(binary1 ^ binary2)
    # strip 0x and L
    return hexxor[2:-1]

print fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
