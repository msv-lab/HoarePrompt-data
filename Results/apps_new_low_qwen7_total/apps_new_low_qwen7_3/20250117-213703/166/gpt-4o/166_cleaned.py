(b, d, s) = map(int, input().split())
max_meals = max(b, d, s)
missed_b = max(0, max_meals - 1 - b)
missed_d = max(0, max_meals - 1 - d)
missed_s = max(0, max_meals - 1 - s)
total_missed_meals = missed_b + missed_d + missed_s
print(total_missed_meals)