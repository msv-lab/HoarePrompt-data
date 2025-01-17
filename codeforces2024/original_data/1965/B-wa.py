t = int(input())
 
for tc in range(t):
    n, k = map(int, input().split())
 
    i = 0
    while (1 << (i + 1)) <= k:
        i = i + 1
 
    ans = [k - (1 << i), k + 1]
    if k!=1:
        ans.append((1 << (i+1))-1)
 
    for j in range(20):
        if j != i:
            ans.append(1 << j);
 
    print(len(ans))
    print(*ans)