n, x = map(int, input().split())
days = list(map(int, input().split()))

hugs = 0
total_days = sum(days)
temp_days = total_days * (x // total_days)

for i in range(n):
    if temp_days >= x:
        break
    hugs += (i + 1)
    x -= days[i]
    temp_days -= days[i]
    
print(hugs)