n = int(raw_input())
a = [int(raw_input()) for _ in xrange(n)]
mxlba = 0
for i in xrange(n):
    mxlba = max(mxlba, len(bin(a[i])[2:]))
cnt = [0] * (mxlba + 5)
for i in xrange(n):
    bit = bin(a[i])[2:]
    lb = len(bit)
    for j in xrange(lb - 1, -1, -1):
        if bit[j] == '1':
            cnt[lb - 1 - j] += 1
            break
axor = 0
for i in xrange(n):
    axor ^= a[i]
if axor == 0:
    print(0)
    exit()
axor = bin(axor)[2:]
la = len(axor)
ans = 0
i = -1
while i < la:
    i += 1
    if axor[i] == '1':
        if cnt[i] == 0:
            print(-1)
            exit()
        else:
            ans += 1
            cnt[i] -= 1
            if la - i - 1 == 0:
                break
            tmp = int('1' * (la - i - 1), 2)
            axor = int(axor, 2) ^ tmp
            axor = bin(axor)[2:]
print(ans)