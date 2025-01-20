# Read input
n = int(input())
a = list(map(int, input().split()))

# Initialize sums
total_sum = sum(a)
min_positive_odd = float('inf')
max_negative_odd = float('-inf')

# Check if the total sum is odd
if total_sum % 2 != 0:
    print(total_sum)
else:
    for num in a:
        if num % 2 != 0:
            if num > 0:
                min_positive_odd = min(min_positive_odd, num)
            else:
                max_negative_odd = max(max_negative_odd, num)
    
    # Calculate possible results by adjusting the total sum to make it odd
    result1 = total_sum - min_positive_odd if min_positive_odd != float('inf') else float('-inf')
    result2 = total_sum - max_negative_odd if max_negative_odd != float('-inf') else float('-inf')

    # Print the maximum valid result
    print(max(result1, result2))
