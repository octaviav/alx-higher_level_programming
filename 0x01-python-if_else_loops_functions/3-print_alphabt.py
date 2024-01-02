#!/usr/bin/python3
for k in range(97, 123):
    if k in [101, 113]:
        continue
    print("{}".format(chr(k)), end='')
