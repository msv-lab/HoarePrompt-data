# Read input values
n, k = map(int, input().split())
s = input()

# Count the occurrences of each balloon color
color_count = {}
for color in s:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

# Check if any color count exceeds the number of friends
can_distribute = True
for count in color_count.values():
    if count > k:
        can_distribute = False
        break

# Print the result
if can_distribute:
    print("YES")
else:
    print("NO")
