#!/usr/bin/python3
for a in range(122, 96, -1):
    print("{:c}".format((a - 32) if a % 2 != 0 else a), end="")
