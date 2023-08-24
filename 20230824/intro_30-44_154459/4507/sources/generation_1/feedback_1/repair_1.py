
# Function to calculate the minimum cost of buying k shovels
def calculate_minimum_cost(n, m, k, shovel_costs, special_offers):
    # Sort the shovel costs in ascending order
    shovel_costs.sort()

    # Initialize the total cost and the number of shovels bought
    total_cost = 0
    num_bought = 0

    # Iterate through the special offers in descending order of y
    for i in range(m - 1, -1, -1):
        num_to_buy = special_offers[i][0]
        num_free = special_offers[i][1]

        # Calculate the cost for this special offer
        if num_free < num_to_buy:
            cost = sum(shovel_costs[num_bought:num_bought + num_to_buy - num_free])
        else:
            cost = sum(shovel_costs[num_bought + num_free:num_bought + num_to_buy])

        # Update the total cost and the number of shovels bought
        total_cost += cost
        num_bought += num_to_buy

    # Check if there are more shovels to be bought
    if n - num_bought < k:
        # Calculate the cost for the remaining shovels
        cost = sum(shovel_costs[num_bought:])
        total_cost += cost
    else:
        # Calculate the cost for the remaining k shovels
        cost = sum(shovel_costs[num_bought:num_bought + k])
        total_cost += cost

    # Return the minimum cost
    return total_cost

# Read the input
n, m, k = map(int, input().split())
shovel_costs = list(map(int, input().split()))
special_offers = []
for _ in range(m):
    special_offers.append(list(map(int, input().split())))

# Calculate the minimum cost
minimum_cost = calculate_minimum_cost(n, m, k, shovel_costs, special_offers)

# Print the minimum cost
print(minimum_cost)
