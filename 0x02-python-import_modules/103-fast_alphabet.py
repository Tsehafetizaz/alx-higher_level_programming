#!/usr/bin/python3
import string
print(*map(chr, range(ord(string.ascii_uppercase[0]), ord(string.ascii_uppercase[-1])+1)), sep='')
