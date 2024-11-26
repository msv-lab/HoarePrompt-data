from math import factorial # python math library

#strnumbers = str(lst)
#listnumbers = list(strnumbers.split())
a,b = raw_input().split()
n = int(a)
i = int(b)   
i = i-1               # n is the length of the permutation
p = range(1, n + 1) # p is a list from 1 to n

for k in range(1, n + 1): # k goes from 1 to n
    f = factorial(n - k)  # compute factorial once per iteration
    d = i // f            # use integer division (like division + floor)
    print(p[d]),          # print permuted number with trailing space
    p.remove(p[d])        # delete p[d] from p
    i = i % f       