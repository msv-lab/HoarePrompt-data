n = int(input())

# Calculate full weeks and the remainder days
full_weeks = n // 7
remainder_days = n % 7

# Max days off is when the remainder days are all days off (maximum 2 days off)
max_days_off = full_weeks * 2 + min(remainder_days, 2)

# Min days off is when the remainder days are all work days, but if there are more than 5 remainder days, the extra are days off
min_days_off = full_weeks * 2 + max(0, remainder_days - 5)

print(min_days_off, max_days_off)
