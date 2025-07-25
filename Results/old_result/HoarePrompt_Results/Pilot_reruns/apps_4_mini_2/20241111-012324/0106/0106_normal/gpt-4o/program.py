# Function to calculate minimum time for Edward to reach Natasha's apartment
def min_time_to_reach(n, m, k, a, b):
    # Calculating block, floor, and apartment within floor for both apartments
    def get_location(apartment):
        block = (apartment - 1) // (m * k) + 1
        floor_within_block = (apartment - 1) % (m * k)
        floor = floor_within_block // k + 1
        return block, floor

    block_a, floor_a = get_location(a)
    block_b, floor_b = get_location(b)
    
    # Time to get from floor_a to floor 1 using the elevator
    if floor_a == 1:
        time_to_exit = 0
    else:
        time_to_exit = 10 + (floor_a - 1)
    
    # Time to walk between the blocks
    direct_walk_time = (abs(block_a - block_b) % n) * 15
    reverse_walk_time = (n - abs(block_a - block_b)) % n * 15
    min_walk_time = min(direct_walk_time, reverse_walk_time)

    # Time to go from floor 1 in block_b to floor_b
    time_to_target_floor = (floor_b - 1) * 5
    
    # Total time
    total_time = time_to_exit + min_walk_time + time_to_target_floor
    return total_time

# Reading input
n, m, k = map(int, input().split())
a, b = map(int, input().split())

# Computing the result
result = min_time_to_reach(n, m, k, a, b)

# Printing the result
print(result)
