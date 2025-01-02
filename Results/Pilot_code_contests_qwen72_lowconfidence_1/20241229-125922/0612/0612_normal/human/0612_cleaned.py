def func_1(arr):
    fwtree = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        func_2(fwtree, i, arr[i])
    return fwtree

def func_2(fwtree, i, val):
    i += 1
    while i < len(fwtree):
        fwtree[i] += val
        i += i & -i

def func_3(fwtree, i):
    s = 0
    i += 1
    while i > 0:
        s += fwtree[i]
        i -= i & -i
    return s
mod = 998244353
fac = [1]
for i in range(1, 200010):
    fac.append(i * fac[-1] % mod)
facInv = []
for i in fac:
    facInv.append(pow(i, mod - 2, mod))
n = input()
p = list(map(lambda x: int(x) - 1, raw_input().split()))
numMissing = len([x for x in p if x == -2])
A = [0 for i in range(n)]
A = func_1(A)
cnt = 0
for i in p:
    if i == -2:
        continue
    cnt += func_3(A, n - 1) - func_3(A, i)
    func_2(A, i, 1)
cnt *= fac[numMissing]
cntNeg = 0
for i in p:
    if i == -2:
        cntNeg += 1
        continue
    missingGreater = n - i - 1 - (func_3(A, n - 1) - func_3(A, i))
    missingSmaller = i - func_3(A, i - 1)
    missingLeftPos = cntNeg
    missingRightPos = numMissing - cntNeg
    cnt += fac[numMissing - 1] * missingGreater * missingLeftPos + fac[numMissing - 1] * missingSmaller * missingRightPos
cnt += fac[numMissing] * numMissing * (numMissing - 1) / 4
cnt %= mod
print(cnt * facInv[numMissing] % mod)