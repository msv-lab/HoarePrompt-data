def count_equal_choices(N, difficulties):
    # Initialize counter for number of choices
    num_choices = 0
    
    # Iterate over all possible values of K
    for K in range(1, max(difficulties) + 1):
        # Initialize counters for ARCs and ABCs
        count_ARCs = 0
        count_ABCs = 0
        
        # Count the number of problems for ARCs and ABCs
        for d in difficulties:
            if d >= K:
                count_ARCs += 1
            else:
                count_ABCs += 1
        
        # Check if the counts for ARCs and ABCs are equal
        if count_ARCs == count_ABCs:
            num_choices += 1
    
    return num_choices

# Read input
N = int(input())
difficulties = list(map(int, input().split()))

# Get the number of choices of K
num_choices = count_equal_choices(N, difficulties)

# Print the result
print(num_choices)