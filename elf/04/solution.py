#!/usr/bin/env python

# there is a specific string that gets loaded:
# 401687 !   mov         qword ptr [rbp-18h], strz_G3R0054731720_40199e
# 40199e
# ......   strz_G3R0054731720_40199e:      ;xref o401687
# ......     db          "G3R0054731720\0"

# this string gets xor'ed with:
# 401144 !   mov         byte ptr [rbp-10h], 9
# 401148 !   mov         byte ptr [rbp-0fh], 3
# 40114c !   mov         byte ptr [rbp-0eh], 6
# 401150 !   mov         byte ptr [rbp-0dh], 5
# 401154 !   mov         byte ptr [rbp-0ch], 0
# 401158 !   mov         byte ptr [rbp-0bh], 5dh
# 40115c !   mov         byte ptr [rbp-0ah], 0
# 401160 !   mov         byte ptr [rbp-9], 45h
# 401164 !   mov         byte ptr [rbp-8], 57h
# 401168 !   mov         byte ptr [rbp-7], 4bh
# 40116c !   mov         byte ptr [rbp-6], 7
# 401170 !   mov         byte ptr [rbp-5], 40h
# 401174 !   mov         byte ptr [rbp-4], 4ah

s="G3R0054731720"
arr=[9,3,6,5,0,0x5d,0,0x45,0x57,0x4b,7,0x40,0x4a]

sol=""
for i in xrange(len(s)):
	sol += chr( ord(s[i]) ^ arr[i] )
print sol

