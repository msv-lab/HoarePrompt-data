import math

A, I = map(int, input().split())

scientists = (A * I) - (A - 1)

print(math.ceil(scientists))