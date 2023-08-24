n = int(input())
denominations = list(map(int, input().split()))

# Check if the coin system is canonical or non-canonical
def check_canonical(denominations):
    # Calculate the sum of the two largest denominations
    max_sum = denominations[-1] + denominations[-2]
    
    # Check if the sum of any two denominations is greater than max_sum
    for i in range(n):
        for j in range(i+1, n):
            if denominations[i] + denominations[j] <= max_sum:
                return "non-canonical"
    return "canonical"

# Print the result
print(check_canonical(denominations))