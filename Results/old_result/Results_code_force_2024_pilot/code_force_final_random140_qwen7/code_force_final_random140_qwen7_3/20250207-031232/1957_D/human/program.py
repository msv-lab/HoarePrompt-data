def solve():
    # print('-----------------')
    n = int(input())
    arr = list(map(int,input().split()))
    # 显然需要把子段异或和转化成前缀异或和
    prefix = [0]
    for v in arr:
        prefix.append(v ^ prefix[-1])
    # print(arr,prefix)
    # 前后缀分解
    pre = [[0, 0] for _ in range(32)]
    suf = [[0, 0] for _ in range(32)]
    for i in range(32):
        pre[i][0] += 1
 
    for i in range(n, 0, -1):
        cur = prefix[i]
        for j in range(32):
            if cur >> j & 1:
                suf[j][1] += 1
            else:
                suf[j][0] += 1
    # print(pre)
    # print(suf)
    ans = 0
    for i in range(1, n + 1):
        y = arr[i - 1]
        # 最高位1
        k = y.bit_length() - 1
        ans += pre[k][0] * suf[k][0] + pre[k][1] * suf[k][1]
        c = prefix[i]
        for j in range(32):
            if c >> j & 1:
                pre[j][1] += 1
                suf[j][1] -= 1
            else:
                pre[j][0] += 1
                suf[j][0] -= 1
    print(ans)
T=int(input())
for _ in range(T):
    solve()