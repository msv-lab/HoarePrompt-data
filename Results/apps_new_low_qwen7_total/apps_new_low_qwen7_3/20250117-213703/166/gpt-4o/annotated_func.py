#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

max_meals = max(b, d, s)

missed_b = max(0, max_meals - 1 - b)

missed_d = max(0, max_meals - 1 - d)

missed_s = max(0, max_meals - 1 - s)

total_missed_meals = missed_b + missed_d + missed_s

print(total_missed_meals)
#Overall this is what the function does:The function reads three non-negative integers \(b\), \(d\), and \(s\) from the standard input, where each integer is between 0 and \(10^{18}\), and their sum is at least 1. It calculates the maximum number of meals (each meal requiring one unit of \(b\), \(d\), or \(s\)) that can be served based on the available resources. For each resource type, it computes the number of meals that could have been served but were missed due to insufficient resources. Finally, it prints the total number of missed meals. Potential edge cases include when one or more of the inputs are zero, which still allows for the calculation of missed meals. The function does not handle invalid input types or values outside the specified range.

