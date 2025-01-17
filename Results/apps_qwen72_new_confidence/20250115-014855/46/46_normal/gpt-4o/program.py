def find_sequence(n, k):
    min_sum = k * (k + 1) // 2  # Sum of the first k natural numbers
    
    if min_sum > n:
        return -1
    
    d = n // min_sum  # Maximum possible GCD
    remainder = n - d * min_sum
    
    sequence = [d * (i + 1) for i in range(k)]
    
    # Distribute the remainder to the sequence to make the sum equal to n
    for i in range(k-1, -1, -1):
        if remainder == 0:
            break
        sequence[i] += 1
        remainder -= 1
    
    return sequence

# Read input
n, k = map(int, input().split())

result = find_sequence(n, k)
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
