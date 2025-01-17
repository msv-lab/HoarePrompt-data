def find_max_y(n, k):
    count = 0                     # Counter for the number of paths containing y
    current_y = n                 # Start from the highest number and move down
    while current_y > 0:
        if current_y % 2 == 1:    # If current_y is odd
            next_y = current_y - 1
        else:                     # If current_y is even
            next_y = current_y // 2

        # Calculate how many numbers in the range [1, n] include current_y in their path
        count += (n - current_y) // current_y + 1

        if count >= k:
            return current_y

        current_y = next_y

    return 1                      # If no such y is found, return 1

# Read input
import sys
input = sys.stdin.read
n, k = map(int, input().split())

# Print the result
print(find_max_y(n, k))
