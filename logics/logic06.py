#!/usr/bin/env python

# distance: d=downhill, f=flat, u=uphill
# 1) d/90 + f/80 + u/72 = 3h
# 2) d/72 + f/80 + u/90 = 3,5h
# convert mph to mpm and h to m
# 1) 2d/3 + 3f/4 + 5u/6 = 180m
# 2) 5d/6 + 3f/4 + 2u/3 = 210m
# simplify (*12)
# 1) 8a + 9b + 10c = 2160m
# 2) 10a + 9b + 8c = 2520m

F_TO_M = 2160
M_TO_F = 2520

DMAX = min(  F_TO_M//8, M_TO_F//10 ) + 1
FMAX = min(  F_TO_M//9,  M_TO_F//9 ) + 1
UMAX = min( F_TO_M//10,  M_TO_F//8 ) + 1

for d in xrange(DMAX):
	for f in xrange(FMAX):
		for u in xrange(UMAX):
			if 8*d+9*f+10*u != F_TO_M: continue
			if 10*d+9*f+8*u != M_TO_F: continue
			print d+f+u, d, f, u
