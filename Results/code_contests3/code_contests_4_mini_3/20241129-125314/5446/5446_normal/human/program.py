from math import ceil

n, b, c = [int(x) for x in raw_input().split()]

x = max(b,c) / float(min(b,c))

print (int(ceil(min(b,c)/float(n)*x)))
