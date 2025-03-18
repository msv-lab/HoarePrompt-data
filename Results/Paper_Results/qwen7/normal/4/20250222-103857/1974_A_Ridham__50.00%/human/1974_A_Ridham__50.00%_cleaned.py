n = int(input())
result = []
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    space_x = x * 1
    space_y = y * 4
    total_space = space_y + space_x
    if y % 2 == 0:
        screen_require_for_y = y // 2
    else:
        screen_require_for_y = y // 2 + 1
    remaining_cells = 15 * screen_require_for_y - space_y
    if space_x <= remaining_cells:
        result.append(screen_require_for_y)
    else:
        extra_space = space_x - remaining_cells
        if space_x % 15 == 0:
            extra_screen = space_x // 15
        else:
            extra_screen = extra_space // 15 + 1
        result.append(extra_screen + screen_require_for_y)
print('\n'.join(map(str, result)))