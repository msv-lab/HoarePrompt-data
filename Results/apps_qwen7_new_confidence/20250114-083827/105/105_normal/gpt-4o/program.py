n = int(input())
a = list(map(int, input().split()))

total_problems = sum(a)
half_problems = (total_problems + 1) // 2

current_sum = 0
for i in range(n):
    current_sum += a[i]
    if current_sum >= half_problems:
        print(i + 1)
        break
