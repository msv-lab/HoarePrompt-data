def calculate_ways(X, N, cars):
    # Initialize count of ways to 0
    ways = 0
    # Iterate over each car
    for car in cars:
        # Initialize counter for compartments with X free places
        compartment_count = 0
        # Iterate over each compartment in the car
        for i in range(45):
            # Check if all places in the compartment are free
            if car[i] != '1' and car[i+1] != '1' and car[i+2] != '1' and car[i+3] != '1' and car[i+45] != '1' and car[i+46] != '1':
                # Increment compartment count
                compartment_count += 1
        # Multiply compartment count by X to get number of ways to sell X tickets in one car
        ways += compartment_count * X
    # Multiply total number of ways by N to get total number of ways in all cars
    ways *= N
    # Return total number of ways
    return ways

# Read input values
X, N = map(int, input().split())
cars = [input() for _ in range(N)]

# Calculate and print the number of ways to sell the friends exactly X tickets in one compartment
print(calculate_ways(X, N, cars))