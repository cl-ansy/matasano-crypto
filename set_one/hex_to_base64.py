#!/usr/bin/env python
# Convert hex to base64
from binascii import unhexlify, b2a_base64

def hex_to_base64(hexstr):
    # convert hex string to binary
    binary = unhexlify(hexstr)
    # convert binary to base64
    base64str = b2a_base64(binary)

    return base64str

print hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
