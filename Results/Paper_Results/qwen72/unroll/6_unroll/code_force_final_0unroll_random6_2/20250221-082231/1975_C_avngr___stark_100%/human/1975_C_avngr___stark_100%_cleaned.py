t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 2:
        print(min(a))
        continue
    max = 0
    for i in range(n - 2):
        temp = a[i:i + 3]
        temp.sort()
        if temp[1] > max:
            max = temp[1]
    print(max)