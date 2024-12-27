from __future__ import print_function, division
input = raw_input


m = int(input())
a = map(int, input().split())

cur_h = 0
n = int(input())
for i in xrange(n):
    w, h = map(int, input().split())
    ch = a[w-1]    
    if ch > cur_h:
        print(ch)
        cur_h = ch + h
    else:
        print(cur_h)
        cur_h += h
        
    
