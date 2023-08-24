n, x = map(int, input().split())
days = list(map(int, input().split()))

hugs = 0
total_days = sum(days)
for i in range(n):
    temp_days = total_days * (x // total_days)
    for j in range(days[i]):
        if temp_days >= x:
            break
        hugs += (i + 1)
        x -= 1
        temp_days -= 1

print(hugs)