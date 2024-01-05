#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    nom = dir()
    for k in range(0, len(nom)):
        if nom[k][:2] != "__":
            print("{:s}".format(nom[k]))
