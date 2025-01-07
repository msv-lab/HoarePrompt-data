def func_1(n, operations, x, y):
    final_x = 0
    final_y = 0
    for op in operations:
        if op == 'U':
            final_y += 1
        elif op == 'D':
            final_y -= 1
        elif op == 'L':
            final_x -= 1
        elif op == 'R':
            final_x += 1
    dx = x - final_x
    dy = y - final_y
    if dx == 0 and dy == 0:
        return 0
    min_length = float('inf')
    current_x = 0
    current_y = 0
    position_map = {(0, 0): -1}
    for i in range(n):
        if operations[i] == 'U':
            current_y += 1
        elif operations[i] == 'D':
            current_y -= 1
        elif operations[i] == 'L':
            current_x -= 1
        elif operations[i] == 'R':
            current_x += 1
        target_pos = (current_x + dx, current_y + dy)
        if target_pos in position_map:
            min_length = min(min_length, i - position_map[target_pos])
        position_map[current_x, current_y] = i
    return min_length if min_length != float('inf') else -1
n = int(input())
operations = input().strip()
(x, y) = map(int, input().split())
result = func_1(n, operations, x, y)
print(result)