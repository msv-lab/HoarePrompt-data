n, e = map(int, input().split())

count = 0

for num in range(n+1):
    if str(2**e) in str(num):
        count += 1

print(count)