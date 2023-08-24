def calculate_ways(X, N, cars):
    # Initialize count of ways to 0
    ways = 0
    # Iterate over each car
    for car in cars:
        # Initialize counter for compartments with X free places
        compartment_count = 0
        # Iterate over each compartment in the car
        for i in range(9):
            # Check if all places in the compartment are free
            if car[i] == '0' and car[i+1] == '0' and car[i+2] == '0' and car[i+3] == '0' and car[i+45] == '0' and car[i+46] == '0':
                # Increment compartment count
                compartment_count += 1
        # Multiply compartment count by X to get number of ways to sell X tickets in one car
        ways += compartment_count * X
    # Return total number of ways
    return ways

# Read input values
X, N = map(int, input().split())
cars = [input() for _ in range(N)]

# Calculate and print the number of ways to sell the friends exactly X tickets in one compartment
print(calculate_ways(X, N, cars))