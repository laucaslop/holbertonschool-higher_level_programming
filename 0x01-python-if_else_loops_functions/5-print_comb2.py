#!/usr/bin/python3
for c in range(0, 100):
        if c < 99:
            print("{:02d},".format(c), end=" ")
        elif c == 99:
            print("99")
