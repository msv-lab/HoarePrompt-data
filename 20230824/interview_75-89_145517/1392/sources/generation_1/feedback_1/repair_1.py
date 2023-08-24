n, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(input()))

count = 0
for num in a:
    if set(str(num)) <= set(map(str, range(k+1))):
        count += a.count(num)

print(count)