n = int(input())
beauties = list(map(int, input().split()))

max_diff = max(beauties) - min(beauties)

count_max_diff = beauties.count(max(beauties)) * beauties.count(min(beauties))

if max_diff == 0:
    count_max_diff = int(n * (n - 1) / 2)

print(max_diff, count_max_diff)