# Reading input
n, m, a, b = map(int, input().split())

# Calculating the remainder of n divided by m
remainder = n % m

# If n is already divisible by m, no cost is needed
if remainder == 0:
    print(0)
else:
    # Calculating the cost to add boxes
    add_boxes_cost = (m - remainder) * a
    # Calculating the cost to remove boxes
    remove_boxes_cost = remainder * b

    # Output the minimum cost
    print(min(add_boxes_cost, remove_boxes_cost))
