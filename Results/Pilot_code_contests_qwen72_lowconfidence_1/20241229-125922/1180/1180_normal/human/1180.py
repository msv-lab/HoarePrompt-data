n = int(raw_input())
values = raw_input().split()
for i in range(0, n//2, 2):
    j = n-1-i
    values[i], values[j] = values[j], values[i]
print(' '.join(values))
