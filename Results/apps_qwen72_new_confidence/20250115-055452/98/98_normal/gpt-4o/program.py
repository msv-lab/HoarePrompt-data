n, m, x, y, v_x, v_y = map(int, input().split())

def reflect_coordinate(coord, max_val, velocity):
    if velocity == 0:
        return coord

    reflections = (coord + max_val) // max_val
    if reflections % 2 == 0:
        return coord % max_val
    else:
        return max_val - (coord % max_val)

final_x = reflect_coordinate(x, n, v_x)
final_y = reflect_coordinate(y, m, v_y)

if (final_x == 0 or final_x == n) and (final_y == 0 or final_y == m):
    print(final_x, final_y)
else:
    print(-1)
