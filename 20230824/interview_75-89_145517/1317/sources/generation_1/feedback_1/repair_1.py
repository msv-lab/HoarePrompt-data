n, m = map(int, input().split())

if m == 1:
    print(n*n)
    exit()

unique_sums = set()
for i in range(1, n+1):
    for j in range(1, n+1):
        unique_sums.add(i**2 + j**2)

count = 0
for sum in unique_sums:
    if sum % m == 0:
        count += 1

print(count)