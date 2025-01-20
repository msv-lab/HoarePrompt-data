b, d, s = map(int, input().split())

# Find the maximum number of meals taken in any category
max_meals = max(b, d, s)

# Calculate the potential missed meals for each category
missed_b = max(0, max_meals - 1 - b)
missed_d = max(0, max_meals - 1 - d)
missed_s = max(0, max_meals - 1 - s)

# The total number of missed meals is the sum of missed meals in each category
total_missed_meals = missed_b + missed_d + missed_s

print(total_missed_meals)
