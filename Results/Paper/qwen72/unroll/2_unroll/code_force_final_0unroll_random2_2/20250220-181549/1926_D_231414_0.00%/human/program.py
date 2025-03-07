times = int(input())
check = 2**31 -1
for _ in range(times):
    n = int(input())
    data = list(map(int,input().split()))
    dic = dict()
    ans = n
    check =  2**31-1
    for i in data:
        s=i^check
        if s in dic:
            dic[s] -= 1
            ans -= 1
            if dic[s] == 0:
                del(dic[s])
        else:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(ans)