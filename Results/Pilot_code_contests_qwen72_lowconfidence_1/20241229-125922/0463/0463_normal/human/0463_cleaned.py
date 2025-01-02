n = input()
spg = [0] * (n + 1)
xor = [0] * (n + 1)
for i in range(3, n + 1):
    k = 2
    movs = set()
    while k * (k + 1) <= 2 * i:
        s = 2 * i - k * (k - 1)
        if s % (2 * k) == 0:
            a = s / 2 / k
            movs.add(xor[a + k - 1] ^ xor[a - 1])
        k += 1
    mex = 0
    while mex in movs:
        mex += 1
    spg[i] = mex
    xor[i] = xor[i - 1] ^ mex
if spg[n]:
    k = 2
    while k * (k + 1) <= 2 * i:
        s = 2 * i - k * (k - 1)
        if s % (2 * k) == 0:
            a = s / 2 / k
            if xor[a + k - 1] ^ xor[a - 1] == 0:
                break
        k += 1
    print(k)
else:
    print(-1)