t = int(input())
for _ in range(t):
    n = int(input())
    x = n
    pi = n
    result = [0] * n
    ls = list(map(int, input().split()))
    for i in range(n,0,-1):
        x = min(pi,i)
        pi = x - ls[i - 1]
        result[i - 1] = pi
    for j in result:
        print(j,end = ' ')
    print()