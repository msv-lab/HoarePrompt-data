times = int(input())
check = 2 ** 31 - 1
for _ in range(times):
    n = int(input())
    data = list(map(int, input().split()))
    dic = dict()
    ans = 0
    check = 2 ** 31 - 1
    for i in data:
        s = i ^ check
        if i in dic:
            dic[i] -= 1
            if dic[i] == 0:
                del dic[i]
        else:
            if s not in dic:
                dic[s] = 0
            dic[s] += 1
            ans += 1
    print(ans)