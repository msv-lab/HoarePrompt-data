from functools import lru_cache
import math

def count_ways(n, k, S, a):
    # Memoization for the recursive function
    @lru_cache(None)
    def solve(index, remaining_k, remaining_sum):
        if remaining_sum == 0:
            return 1
        if index == n or remaining_sum < 0:
            return 0
        
        # Don't take current cube
        result = solve(index + 1, remaining_k, remaining_sum)
        
        # Take current cube without factorial
        result += solve(index + 1, remaining_k, remaining_sum - a[index])
        
        # Take current cube with factorial if we have stickers left
        if remaining_k > 0:
            result += solve(index + 1, remaining_k - 1, remaining_sum - math.factorial(a[index]))
            
        return result
    
    return solve(0, k, S)

# Read input
n, k, S = map(int, input().split())
a = list(map(int, input().split()))

# Get the number of ways
result = count_ways(n, k, S, a)

print(result)
