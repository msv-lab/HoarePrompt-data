t = int(input())
for _ in range(t):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    s = input().strip()

    prod = 1
    for i in range(len(a)):
        prod *= a[i]
    l = 0
    r = len(a)-1
    for i in range(len(s)):
        print(int(prod % m))
        if(s[i] == 'L'):
            prod /= a[l]
            l+=1
        else:
            prod /= a[r]
            r -=1
    print()

