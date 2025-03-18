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
    for i in range(cur):
        if M[i] <= i:
            cur = i
            break
    print(cur)