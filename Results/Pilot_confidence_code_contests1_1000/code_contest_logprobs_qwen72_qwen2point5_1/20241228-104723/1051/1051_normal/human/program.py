from __future__ import print_function
n = int(input())
x, y = 1, 2
for i in range(n-1):
    x, y = y, x + y
s, t = bin(y)[2:][::-1], bin(x)[2:][::-1]
print(len(s) - 1)
for c in s:
    print(c, end=' ')
print()
print(len(t) - 1)
for c in t:
    print(c, end=' ')
print()