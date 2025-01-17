n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    c = (a*(a-1))//2
    if c - b >= a - 1:
        print(a)
    else:
        print(1)