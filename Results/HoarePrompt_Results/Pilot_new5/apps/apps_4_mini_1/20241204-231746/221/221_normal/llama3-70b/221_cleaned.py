(s, x) = map(int, input().split())
count = 0
for a in range(1, s):
    b = s - a
    if a ^ b == x:
        count += 1
print(count)