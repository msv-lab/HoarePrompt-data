n = int(input())
beauties = list(map(int, input().split()))

beauties.sort()

max_diff = beauties[n-1] - beauties[0]

count_max_diff = 0

if max_diff == 0:
    count_beauty = {}
    for beauty in beauties:
        count_beauty[beauty] = count_beauty.get(beauty, 0) + 1
    for count in count_beauty.values():
        count_max_diff += count * (count - 1) // 2
else:
    count_max_diff = beauties.count(beauties[0]) * beauties.count(beauties[n-1])

print(max_diff, count_max_diff)