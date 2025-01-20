#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

max_meals = max(b, d, s)

missed_b = max(0, max_meals - 1 - b)

missed_d = max(0, max_meals - 1 - d)

missed_s = max(0, max_meals - 1 - s)

total_missed_meals = missed_b + missed_d + missed_s

print(total_missed_meals)
#Overall this is what the function does:The function reads three non-negative integers \( b \), \( d \), and \( s \) from the input, where each integer is between 0 and \( 10^{18} \), inclusive, and their sum is at least 1. It then calculates the number of meals that could have been taken by each individual (represented by \( b \), \( d \), and \( s \)) but were missed due to constraints, assuming a maximum of one meal can be taken per individual. Specifically, it computes the number of missed meals for each individual as the maximum of zero and the difference between the maximum allowed meals (1) and the actual meals taken. Finally, it sums up the missed meals across all individuals and prints the total number of missed meals.

