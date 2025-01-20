s = input().strip()
n = int(s[:-1])
seat = s[-1]

# Determine the base time for the row
group = (n - 1) // 4
base_time = group * 8 * 3  # Each group of 4 rows takes 24 seconds (8 per row)

# Determine the extra time within the group
row_position_in_group = (n - 1) % 4
if row_position_in_group == 0 or row_position_in_group == 2:
    base_time += 0  # for rows 1 and 3 in their respective 4-row groups
elif row_position_in_group == 1 or row_position_in_group == 3:
    base_time += 7  # for rows 2 and 4 in their respective 4-row groups

# Determine the time based on the seat position
seat_time = {
    'f': 0,
    'e': 1,
    'd': 2,
    'c': 3,
    'b': 4,
    'a': 5
}[seat]

# Total time is base time plus seat time plus 1 second to start serving
total_time = base_time + seat_time + 1

print(total_time)
