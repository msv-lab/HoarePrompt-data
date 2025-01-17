n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i in a:
    if ans % 2 == 0 and i % 2 != 0:
        ans += i
    elif ans % 2 != 0 and i % 2 == 0:
        ans += i
    elif ans % 2 == 0 and i % 2 == 0:
        ans += i
print(ans)
