from sys import stdin
from string import ascii_lowercase

def readints():
    return map(int, stdin.readline().split())


n, k = readints()
steps = sorted(stdin.readline().strip())
w = 0
i = 0
nb = 0
while i < n and nb < k:
    step = steps[i]
    w += (ascii_lowercase.index(step) + 1)
    i += 2
    nb += 1

print -1 if nb != k else w