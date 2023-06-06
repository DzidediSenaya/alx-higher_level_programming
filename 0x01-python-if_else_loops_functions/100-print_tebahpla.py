#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c + 32 if c % 2 == 0 else c)), end="")
