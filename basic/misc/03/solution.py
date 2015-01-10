#!/usr/bin/env python

import re
from itertools import permutations

REGEX=[ "^[A-Za-z0-9]{5}",
	"^[^e-z0-9A-Z]+[^A-Z]{4}{?[a-z]*_?",
	"^[A9FbdHh5]+[T]*.{2}_?[a-z]+",
	"^[^YdSeu][r]+[^r]+=?_?[aeiou]+[^pstuvwxyz]+",
	"^(c|a|b|d)+[^A-Za-df-qs-z]{2}{?[^vCXBhq]*[^pqrst]*[a]+[^passwd]*}?",
	"^.*[k0pst]$",
	"^[^0-9A-Z]{5}$"
]

# REGEX[6] indicates it is a 5 character lowercase word
# REGEX[1] indicates the first letter is "a", "b", "c" or "d"
# REGEX[3] indicates the first letter can't be "d", so it can be either "a", "b" or "c"
# REGEX[2] indicates first letter must be "b", "d" or "h" => the only possibility now is "b"
# REGEX[3] indicates the 2nd letter must be am "r"

for perm in permutations("abcdefghijklmnopqrstuvwxyz",3):
	word = "br" + ''.join(perm)
	if re.match(REGEX[0],word) == None: continue
	if re.match(REGEX[1],word) == None: continue
	if re.match(REGEX[2],word) == None: continue
	if re.match(REGEX[3],word) == None: continue
	if re.match(REGEX[4],word) == None: continue
	if re.match(REGEX[5],word) == None: continue
	if re.match(REGEX[6],word) == None: continue
	print word
	break

