import hashlib

# It is an MD5 hash
# A google search reveals that:
# MD5("a72242") == 5845a614b287dc1685c2a516ef9717aa
TARGET = "5845a614b287dc1685c2a516ef9717aa"
word = "a72242".encode()
digest = hashlib.md5(word).hexdigest()
print(digest)
print(TARGET)
