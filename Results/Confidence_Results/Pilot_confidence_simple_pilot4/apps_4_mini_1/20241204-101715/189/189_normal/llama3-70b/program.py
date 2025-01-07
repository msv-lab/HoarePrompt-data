n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

seat = [0] * 8
for i in range(8):
    if i == 0 or i == 7:
        seat[i] = 1
    else:
        seat[i] = 2

ans = "YES"
for i in range(k):
    flag = False
    for j in range(8):
        if a[i] <= seat[j]:
            seat[j] -= a[i]
            flag = True
            break
    if not flag:
        ans = "NO"
        break

print(ans)
