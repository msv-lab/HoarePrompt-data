n, m = map(int, input().split())
h_streets = input()
v_streets = input()

h_west_to_east = [i for i, c in enumerate(h_streets) if c == '>']
h_east_to_west = [i for i, c in enumerate(h_streets) if c == '<']
v_north_to_south = [i for i, c in enumerate(v_streets) if c == 'v']
v_south_to_north = [i for i, c in enumerate(v_streets) if c == '^']

can_reach = True

for i in range(n-1):
    if not (h_west_to_east and h_east_to_west):
        can_reach = False
        break
    if i not in h_west_to_east and i not in h_east_to_west:
        can_reach = False
        break

for i in range(m-1):
    if not (v_north_to_south and v_south_to_north):
        can_reach = False
        break
    if i not in v_north_to_south and i not in v_south_to_north:
        can_reach = False
        break

print("YES" if can_reach else "NO")
