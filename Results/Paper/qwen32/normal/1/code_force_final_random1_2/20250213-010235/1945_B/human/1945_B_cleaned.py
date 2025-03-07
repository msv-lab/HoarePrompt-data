t = int(input())
for i in range(t):
    (a, b, m) = map(int, input().split())
    mn = min(a, b) + m
    if m % a == 0 and m % b == 0 and (a != 1) and (b != 1):
        print(mn // a + mn // b + 1)
    else:
        print(mn // a + mn // b)