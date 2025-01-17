n, x = map(int, input().split())
a = list(map(int, input().split()))

max_sum = max_ending_here = a[0]
max_beauty = max_sum
for num in a[1:]:
    max_ending_here = max(num, max_ending_here + num)
    max_sum = max(max_sum, max_ending_here)
    max_beauty = max(max_beauty, max_sum * x)

print(max(max_sum, max_beauty))
