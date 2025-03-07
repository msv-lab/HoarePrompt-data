t = int(input())
for i in range(t):
    (n, k, m) = map(int, input().split())
    s = input()
    cnt = 0
    cur = 0
    for ss in s:
        cur_ss = ord(ss) - ord('a')
        if cur & 1 << cur_ss == 0:
            cur += 1 << cur_ss
        if cur == (1 << k) - 1:
            cnt += 1
            cur = 0
    if cnt >= n:
        print('YES')
    else:
        print('NO')
        tmp = ''
        ans = chr(ord('a') + k - 1) * cnt
        for i in range(k):
            if cur & 1 << i == 0:
                tmp = chr(ord('a') + i)
        ans += tmp
        ans += 'a' * (n - cnt - 1)
        print(ans)