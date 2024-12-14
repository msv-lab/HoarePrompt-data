def max_min_pieces(n, a, b):
    low, high = 1, min(a, b) + 1

    def can_distribute(x):
        return (a // x) + (b // x) >= n

    while low < high:
        mid = (low + high) // 2
        if can_distribute(mid):
            low = mid + 1
        else:
            high = mid
    
    return low - 1

# Read input values
n, a, b = map(int, input().split())

# Compute and print the result
print(max_min_pieces(n, a, b))
