n = int(input())
t = 0
for i in range(n):
    (a, b) = map(int, input().split())
    if a < b:
        print(a, b)
    elif a == b:
        print(a, b)
    else:
        print(b, a)