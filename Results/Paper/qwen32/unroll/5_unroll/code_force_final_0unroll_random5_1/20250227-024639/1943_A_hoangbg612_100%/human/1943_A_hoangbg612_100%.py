T = int(input())
for _ in range(T):
    S = int(input())
    N = list(map(int, input().split()))
    N.sort()
    cur = -1
    M = {}
    for num in N:
        if num > cur:
            if num > cur+1:
                cur += 1
                break
            cur = num
            M[cur] = 1
        else:
            M[cur] += 1
    if sum([M[k] for k in M.keys()]) == S:
        cur += 1
    cnt = []
    for k in M.keys():
        if M[k] == 1:
            cnt.append(k)
    if len(cnt) >= 2:
        cur = cnt[1]
    print(cur)