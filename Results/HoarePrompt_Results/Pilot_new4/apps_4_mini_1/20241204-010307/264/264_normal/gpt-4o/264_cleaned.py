n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
initial_max = max(a)
total_people = sum(a)
max_k = initial_max + m
min_k = (total_people + m + n - 1) // n
print(min_k, max_k)