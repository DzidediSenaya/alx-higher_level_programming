#!/usr/bin/python3

for c in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(c if c % 2 == 1 else c - 32)), end='')
