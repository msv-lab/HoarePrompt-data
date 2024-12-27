import sys

x, y = [int(x) for x in sys.stdin.readline().split()]
string = sys.stdin.readline().strip()
mod_positions, cur_position = [], (0, 0)
for char in string:
    mod_positions.append(cur_position)
    if char=='L':
        cur_position = (cur_position[0]-1, cur_position[1])
    if char=='R':
        cur_position = (cur_position[0]+1, cur_position[1])
    if char=='U':
        cur_position = (cur_position[0], cur_position[1]+1)
    if char=='D':
        cur_position = (cur_position[0], cur_position[1]-1)
dx, dy  = cur_position[0], cur_position[1]
#print(mod_positions, dx, dy)
for position in mod_positions:
    if position[0] == x and position[1] == y:
        print("Yes")
        sys.exit(0)
    if dy != 0 and (y-position[1])%dy == 0:
        n_times = (y-position[1])/dy
        if position[0]+n_times*dx == x and n_times >= 0:
            print("Yes")
            sys.exit(0)
    if dx != 0 and (x-position[0])%dx == 0:
        n_times = (x-position[0])/dx
        if position[1]+n_times*dy == y and n_times >= 0:
            print("Yes")
            sys.exit(0)
print("No")
