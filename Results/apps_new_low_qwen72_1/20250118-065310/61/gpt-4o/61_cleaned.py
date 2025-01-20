s = input().strip()
n = int(s[:-1])
seat = s[-1]
group = (n - 1) // 4
base_time = group * 8 * 3
row_position_in_group = (n - 1) % 4
if row_position_in_group == 0 or row_position_in_group == 2:
    base_time += 0
elif row_position_in_group == 1 or row_position_in_group == 3:
    base_time += 7
seat_time = {'f': 0, 'e': 1, 'd': 2, 'c': 3, 'b': 4, 'a': 5}[seat]
total_time = base_time + seat_time + 1
print(total_time)