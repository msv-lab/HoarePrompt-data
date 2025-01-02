# -*- coding: utf-8 -*-

import sys

u"""
1023回全て check
"""

def ones(n):
    o = 0
    for i in xrange(0, 10):
        b = 1 << i
        if n & b:
            o += 1
    return o

n = int(raw_input().split()[0])
# print n

openL = []
for _ in xrange(0, n):
    fs = ''.join( [e for e in raw_input().split()] )
    openL.append( int(fs, base=2) )
    
profL = []
for _ in xrange(0, n):
    profL.append( [int(e) for e in raw_input().split()] )

# print n
# print [hex(e) for e in openL]
# print profL, len(profL[0])

# print ones(0), ones(0x3ff)

maxP = -sys.maxint - 1
for i in xrange(1, 1024):
    p = 0
    for x in xrange(0, len(openL)):
        ox = openL[x]
        px = profL[x]
        p += px[ ones(ox & i) ]

    if p > maxP:
        maxP = p
    
sys.stdout.write('%d\n' % maxP)
sys.stdout.flush()
