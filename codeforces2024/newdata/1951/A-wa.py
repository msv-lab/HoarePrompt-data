t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if s.count('1')%2 or n == 2:
        print("NO")
    else:
        print("YES")