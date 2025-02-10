t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = {}
    for i in arr:
        counter[i] = counter.get(i, 0) + 1
    ans = 0
    once = False
    for i in range(n):
        if counter.get(i, 0) == 0:
            ans = i
            break
        elif counter.get(i, 0) == 1 and (not once):
            once = True
            ans = i + 1
        elif counter.get(i, 0) == 1:
            ans = i
            break
    print(ans)