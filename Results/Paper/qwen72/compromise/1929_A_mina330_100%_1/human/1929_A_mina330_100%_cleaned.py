ntest = int(input())
for itest in range(0, ntest, 1):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[len(a) - 1] - a[0])