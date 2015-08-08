import sys

#      318330220904692713533  158846 12616105281
#      318338237039211261689  158847 12616264128
TARGET = 318338237039211050000
check = 1337
total = 0
YMAX = 300000
y = 1
while True:
    total += y
    check = 1337 + (total * y**2)
    if check > TARGET:
        print(TARGET)
        print("%21s %d" % (check, y))
        sys.exit()
    y += 1
