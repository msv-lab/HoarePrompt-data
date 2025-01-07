n, k = map(int, input().split())

def are_remainders_distinct(n, k):
    # For k >= n, there will always be non-distinct remainders
    if k >= n:
        return "No"
    
    # For k < n, we'll check for remainders
    seen_remainders = set()
    for i in range(1, k + 1):
        remainder = n % i
        if remainder in seen_remainders:
            return "No"
        seen_remainders.add(remainder)
    
    return "Yes"

print(are_remainders_distinct(n, k))
