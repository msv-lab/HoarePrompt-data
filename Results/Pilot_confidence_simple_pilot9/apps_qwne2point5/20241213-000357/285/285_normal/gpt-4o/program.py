def can_spend_all_coins(n):
    # Define the cost of houses, cars, and computers
    house_cost = 1234567
    car_cost = 123456
    computer_cost = 1234
    
    # Iterate over the possible number of houses
    for a in range(n // house_cost + 1):
        remaining_after_houses = n - a * house_cost
        # Iterate over the possible number of cars
        for b in range(remaining_after_houses // car_cost + 1):
            remaining_after_cars = remaining_after_houses - b * car_cost
            # Check if the remaining coins can be exactly spent on computers
            if remaining_after_cars % computer_cost == 0:
                return "YES"
    
    return "NO"

# Read input
n = int(input().strip())

# Get the result
result = can_spend_all_coins(n)

# Print the result
print(result)
