import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # n = coins
    # k = jewels
    # print(n, k)
    if n == k:
        print("YES")
        print(1)
        print(1)
    elif n % k == 0:
        print("YES")
        print(1)
        print(n//k)
    elif n < k or (k < n and 2*k > (n + 1)):
        print("NO")
    else:
        print("YES")
        print(2)
        # first = math.floor(n/k)
        # second = n - first*k + 2
        # print("SECOND" + str(second))
        first = n - k + 1
        second = 1
        print(str(first) + " " + str(second))

