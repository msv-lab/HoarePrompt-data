t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(1)
    else:
        res = 0
        mdx = n // 2 + n % 2 - 1
        for i in range(mdx, n):
            if a[mdx] == a[i]:
                res += 1
        print(res)