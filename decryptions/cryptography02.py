from base64 import b64decode

s = "VGhpcyBvbmUgd2FzIGJhc2U2NC4gSXQncyBhIGxpdHRsZSBoYXJkZXIgdGhhbiB0aGUgcH"
s += "JldmlvdXMgbWlzc2lvbi4gVGhlID09IG9wZXJhdG9ycyBnaXZlIGJhc2U2NCBhd2F5Lg=="
result = b64decode(s).decode()
print(result)
