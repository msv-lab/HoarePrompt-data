c, d = map(int, input().split())
n, m = map(int, input().split())
k = int(input())

min_problems = 0

# Calculate the number of additional rounds needed
additional_rounds = max(0, n*m - k)
additional_rounds = min(additional_rounds, m)  # Additional rounds should not exceed the available number of participants

# Calculate the number of problems needed for the additional rounds
additional_problems = additional_rounds * d

# Calculate the number of problems needed for the main rounds
main_problems = c * (n - 1)

# Calculate the total number of problems needed
total_problems = additional_problems + main_problems

print(total_problems)