l, r, a = map(int, input().split())

# Step 1: Balance the number of left-handers and right-handers using ambidexters
# First, equalize l and r using ambidexters
if l < r:
    l += min(a, r - l)
    a -= min(a, r - l)
elif r < l:
    r += min(a, l - r)
    a -= min(a, l - r)

# Step 2: If there are still ambidexters left, they should be used in pairs
# Each pair of ambidexters can add 2 to the team, one for each side
max_team_size = l + r + (a // 2) * 2

# Ensure the team size is even
if max_team_size % 2 != 0:
    max_team_size -= 1

print(max_team_size)
