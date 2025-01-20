#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

max_meals = max(b, d, s)

missed_b = max(0, max_meals - 1 - b)

missed_d = max(0, max_meals - 1 - d)

missed_s = max(0, max_meals - 1 - s)

total_missed_meals = missed_b + missed_d + missed_s

print(total_missed_meals)
#Overall this is what the function does:The function takes three non-negative integers \( b \), \( d \), and \( s \) as input, where \( 0 \leq b, d, s \leq 10^{18} \) and \( b + d + s \geq 1 \). It calculates the number of meals that were missed by each type (denoted as \( b \), \( d \), and \( s \)) if each type could have had up to one more meal. Specifically, it computes the maximum possible number of missed meals for each type by comparing the current number of meals with the maximum possible minus one. It then sums these missed meals and prints the total number of missed meals. If any of the inputs \( b \), \( d \), or \( s \) is already at its maximum possible value, the corresponding missed value will be zero. There are no additional actions performed beyond this calculation and output.

