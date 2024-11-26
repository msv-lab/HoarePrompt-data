# -*- coding: utf-8 -*-

W, a, c= map(int,raw_input().split())

b = a + W
d = c + W

if b < c:
    ans = c - b
elif d < a:
    ans = a - d
else:
    ans = 0
    
print(ans)