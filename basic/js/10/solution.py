import sys


def calculate(s, n):
    ret = 0
    for c in s:
        ret += ord(c) * n
        n += 1
    return ret


def search_passwords(passw=""):
    pc = calculate(passw, 3)
    if pc == 2308:
        print(passw)
        sys.exit()  # only one password is enough
    elif pc > 2308:
        return
    else:
        for c in "abcdefghijklmnopqrstuvwxyz":
            search_passwords(passw+c)
            search_passwords(passw+c.upper())

REF = "BHFE8"
REFSUM = calculate(REF, 5)
print(REFSUM)
search_passwords()
