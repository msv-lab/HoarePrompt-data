import math
 
def maximize_gcd_plus_y(t, test_cases):
    results = []
    for x in test_cases:
        max_sum = 0
        best_y = 1
        for y in range(x - 1, 0, -1):
            gcd_val = math.gcd(x, y)
            current_sum = gcd_val + y
            if current_sum > max_sum:
                max_sum = current_sum
                best_y = y
                break
        results.append(best_y)
    return results
 
# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]
 
# Get results
results = maximize_gcd_plus_y(t, test_cases)
 
# Output results
for result in results:
    print(result)