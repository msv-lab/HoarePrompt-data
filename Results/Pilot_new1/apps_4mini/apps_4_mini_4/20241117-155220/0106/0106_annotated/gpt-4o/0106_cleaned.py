def func_1(n, m, k, a, b):

    def get_location(apartment):
        block = (apartment - 1) // (m * k) + 1
        floor_within_block = (apartment - 1) % (m * k)
        floor = floor_within_block // k + 1
        return (block, floor)
    (block_a, floor_a) = get_location(a)
    (block_b, floor_b) = get_location(b)
    if floor_a == 1:
        time_to_exit = 0
    else:
        time_to_exit = 10 + (floor_a - 1)
    direct_walk_time = abs(block_a - block_b) % n * 15
    reverse_walk_time = (n - abs(block_a - block_b)) % n * 15
    min_walk_time = min(direct_walk_time, reverse_walk_time)
    time_to_target_floor = (floor_b - 1) * 5
    total_time = time_to_exit + min_walk_time + time_to_target_floor
    return total_time
(n, m, k) = map(int, input().split())
(a, b) = map(int, input().split())
result = func_1(n, m, k, a, b)
print(result)