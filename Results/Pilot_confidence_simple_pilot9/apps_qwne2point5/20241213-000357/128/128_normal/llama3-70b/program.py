n, f = map(int, input().split())
days = []
for _ in range(n):
    k, l = map(int, input().split())
    days.append((k, l))

days.sort(key=lambda x: x[1] - x[0], reverse=True)

sold = 0
for i in range(n):
    if i < f:
        sold += min(days[i][0] * 2, days[i][1])
    else:
        sold += min(days[i][0], days[i][1])

print(sold)
