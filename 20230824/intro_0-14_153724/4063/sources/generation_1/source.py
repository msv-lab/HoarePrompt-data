def count_even_difficulties(N, difficulties):
    # Count the number of even difficulties
    even_difficulties = sum(1 for d in difficulties if d % 2 == 0)
    
    # Number of choices of K is equal to the number of even difficulties
    return even_difficulties

# Read input
N = int(input())
difficulties = list(map(int, input().split()))

# Get the number of choices of K
num_choices = count_even_difficulties(N, difficulties)

# Print the result
print(num_choices)