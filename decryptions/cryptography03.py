#!/usr/bin/env python

import hashlib

#It is an MD5 hash
#A google search reveals that:
#5845a614b287dc1685c2a516ef9717aa == MD5("a72242")
TARGET="5845a614b287dc1685c2a516ef9717aa"

print hashlib.md5("a72242").hexdigest()
print TARGET
