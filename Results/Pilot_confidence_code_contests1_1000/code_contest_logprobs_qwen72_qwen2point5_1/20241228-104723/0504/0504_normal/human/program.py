

n,k=map(int,raw_input().strip().split())
A=map(int,raw_input().strip().split())

"""
n,k=4,20
A=[10,3,6,3]
"""
A.sort()

c = 0
for ai in A:
    while ai > 2 * k:
        k *= 2
        c += 1
    k = max(k, ai)
print(c)
exit()