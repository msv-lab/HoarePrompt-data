n = int(input())
a = map(int, raw_input().split())
maximum_count = 0
for start in range(0, n):
    for end in range(0, n):
        if start <= end:
            b = list(a)
            for i in range(start, end + 1):
                b[i] = 1 - b[i]
            count = sum(b)
            maximum_count = max(maximum_count, count)
print(maximum_count)