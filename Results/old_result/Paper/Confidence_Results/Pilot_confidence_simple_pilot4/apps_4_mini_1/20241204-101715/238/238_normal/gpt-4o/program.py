def max_pillows(n, m, k):
    def can_distribute(x):
        total_pillows = x
        # Calculate the pillows needed on the left side of Frodo's bed
        if k > 1:
            left = min(k - 1, x - 1)
            total_pillows += left * (left + 1) // 2
            if x - 1 > left:
                total_pillows += (k - 1 - left) * (x - left - 1)
        # Calculate the pillows needed on the right side of Frodo's bed
        if n - k > 0:
            right = min(n - k, x - 1)
            total_pillows += right * (right + 1) // 2
            if x - 1 > right:
                total_pillows += (n - k - right) * (x - right - 1)
        return total_pillows <= m
    
    low, high = 1, m
    while low < high:
        mid = (low + high + 1) // 2
        if can_distribute(mid):
            low = mid
        else:
            high = mid - 1
    return low

# Reading input
n, m, k = map(int, input().strip().split())

# Output the result
print(max_pillows(n, m, k))
